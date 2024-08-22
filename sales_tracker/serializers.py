from rest_framework import serializers
from sales_tracker.models import Store, TrackData, ShopifyStore, UserShopifyStore
from ApiSDK.sales_tracker import SalesTracker
from ScraperSDK.winninghunt import WinningHunt
from django.contrib.auth.models import User
from ScraperSDK import shopify
import logging
import requests

logger = logging.getLogger(__file__)

class AddShopifyStoreByUrlSerializer(serializers.Serializer):
  url=serializers.URLField()
  
  def validate(self, attrs):
    data=attrs
    
    try:
      shop = shopify.Shopify(attrs["url"])
    except Exception as e:
      raise serializers.ValidationError(f"Invalid store, please make sure the provided url is of a shopify store: {str(e)}")
    else:
      data["title"]=shop.title
      data["url"]=shop.url
      data["hostname"]=shop.hostname
      data["themedata"]=shop.themeData
      data["shopify_url"]=shop.shopify_url
      data["locale"]=shop.locale
      data["currency"]=shop.currency

    try:
      store=ShopifyStore.objects.get(url=data["url"])
    except ShopifyStore.DoesNotExist:
      pass
    else:
      raise serializers.ValidationError(f"Store {shop.title} exists!")
      
    return data

  def create(self, validated_data):
    store=ShopifyStore.objects.create(**validated_data)
    return store

class RequestAddUserShopifyStoreByUrlSerializer(serializers.Serializer):
  url=serializers.URLField()
  access_token=serializers.CharField()  

class AddUserShopifyStoreByUrlSerializer(serializers.Serializer):
  url=serializers.URLField()
  access_token=serializers.CharField()
  
  def __init__(self,*args,user:User,**kwargs):
    super().__init__(*args,**kwargs)
    self.user=user
  
  def validate(self,data):
    serializer=AddShopifyStoreByUrlSerializer(data={"url":data["url"]})
    if serializer.is_valid():
      store=serializer.save()
      data["store"]=store
    else:
      raise serializers.ValidationError(serializer.errors)
    
    return data
  
  def create(self,validated_data):
    userStore=UserShopifyStore.objects.create(
      user=self.user,
      store=validated_data["store"],
      access_token=validated_data["access_token"]
    )
    return userStore

class ShopifyStoreSerializer(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  title=serializers.CharField(required=True)
  url=serializers.URLField(required=True)
  hostname=serializers.CharField()
  themedata=serializers.JSONField()
  shopify_url=serializers.CharField()
  locale=serializers.CharField()
  currency=serializers.JSONField()

  def create(self, validated_data):
    store=ShopifyStore.objects.create(**validated_data)
    return store

class UserShopifyStoreSerializer(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  user=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
  store=ShopifyStoreSerializer(many=False)
  access_token=serializers.CharField()
  
  def create(self, validated_data):
    userShopifyStore=ShopifyStore.objects.create(**validated_data)
    return userShopifyStore

class TrackDataSerializer(serializers.Serializer):
  store=serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())
  data=serializers.JSONField()
  
  def create(self, validated_data):
    try:
      trackData = validated_data["store"].track_data
    except TrackData.DoesNotExist:
      trackData = None
    if trackData:
      trackData.data = validated_data["data"]
      trackData.save()
      return trackData
    else:
      trackData=TrackData.objects.create(**validated_data)
      return trackData

class StoreSerializer(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  user=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
  title=serializers.CharField(required=True)
  url=serializers.URLField(required=True)
  hostname=serializers.CharField()
  track_data=TrackDataSerializer(many=False,read_only=True)
  themedata=serializers.JSONField()
  shopify_url=serializers.CharField()
  locale=serializers.CharField()
  currency=serializers.JSONField()

  def create(self, validated_data):
    store=Store.objects.create(**validated_data)
    return store

class StoreAddSerializer(serializers.Serializer):
  url=serializers.CharField()
  
  def __init__(self, user:User, instance=None, data=..., **kwargs):
    super().__init__(instance, data, **kwargs)
    self.user=user

  def validate(self, attrs):
    data=attrs
    
    try:
      shop = shopify.Shopify(data["url"])
    except Exception as e:
      raise serializers.ValidationError(f"Invalid store, please make sure the provided url is of a shopify store: {str(e)}")
    else:
      serializer=StoreSerializer(data={
        "user":self.user.id,
        "title":shop.title,
        "url":shop.url,
        "hostname":shop.hostname,
        "themedata":shop.themeData,
        "shopify_url":shop.shopify_url,
        "locale":shop.locale,
        "currency":shop.currency,
      })
      if serializer.is_valid():
        data=serializer.validated_data

    try:
      store=self.user.stores.get(url=data["url"])
    except Store.DoesNotExist:
      store=None
      
    print(store)
    
    if store:
      raise serializers.ValidationError(f"The store {data['url']} is already being tracked")
      
    return data

  def create(self, validated_data):
    store=Store.objects.create(**validated_data)
    return store

class AddTrackingSiteSerializer(serializers.Serializer):
  url=serializers.URLField()

class ImportProductSerializer(serializers.Serializer):
  product_url=serializers.URLField()
  store_url=serializers.URLField()
  
  def __init__(self,*args,user,**kwargs):
    super().__init__(*args,**kwargs)
    self.user=user
    self.product=None
    self.store=None
  
  def validate(self,data):
    try:
      self.product=shopify.ShopifyProduct(data["product_url"])
    except Exception as e:
      raise serializers.ValidationError(str(e))
    
    try:
      store=shopify.Shopify(data["store_url"])
      self.store=self.user.my_stores.get(store__url=store.url)
    except Exception as e:
      raise serializers.ValidationError(str(e))
    
    return data
  
  def create(self,validated_data):
    response=requests.post(url=f"https://{self.store.store.shopify_url}/admin/api/2024-07/products.json",json={
      "product":{
        "title":self.product.data["title"],
        "body_html":self.product.data["body_html"],
        "vendor":self.product.data["vendor"],
        "product_type":self.product.data["product_type"],
        "status":"draft"
      }
    },headers={
      "X-Shopify-Access-Token":f"{self.store.access_token}",
      "Content-Type":"application/json",
    })
    # logger.info(response.json())
    try:
      data=response.json()
    except Exception as e:
      logger.error(e)
      data={"status":response.status_code,"content":response.text}
      
    return data

class RequestImportProductSerializer(serializers.Serializer):
  product_url=serializers.URLField()
  store_url=serializers.URLField()
 