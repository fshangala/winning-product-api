from rest_framework import serializers
from sales_tracker.models import Store, TrackData, ShopifyStore
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
  
  def validate(self,data):
    try:
      product=shopify.Shopify(validated_data["product_url"])
    except Exception as e:
      raise serializers.ValidationError(str(e))
    
    try:
      store=shopify.Shopify(validated_data["store_url"])
    except Exception as e:
      raise serializers.ValidationError(str(e))
    
    return data
  
  def create(self,validated_data):
    store=self.user.my_stores.get(url=validated_data["store_url"])
    response=requests.post(url=f"{store.store.shopify_url}/admin/api/2024-07/products.json",data={
      "product":{
        "title":store.title,
        "body_html":store.title,
        "vendor":"Burton",
        "product_type":"Snowboard",
        "status":"draft"
      }
    },headers={
      "X-Shopify-Access-Token":f"{store.store.access_token}",
      "Content-Type":"application/json",
    })
    logger.info(response.json())
    return response.json()

    