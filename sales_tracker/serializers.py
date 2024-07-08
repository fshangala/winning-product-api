from rest_framework import serializers
from sales_tracker.models import Store
from ApiSDK.sales_tracker import SalesTracker
from ScraperSDK.winninghunt import WinningHunt
from django.contrib.auth.models import User

class StoreSerializer(serializers.Serializer):
  user=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
  title=serializers.CharField(required=True)
  url=serializers.URLField(required=True)
  hostname=serializers.CharField()

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
    sales_tracker=SalesTracker()
    try:
      shopifyStore = sales_tracker.getStoreData(storeUrl=attrs["url"])
    except Exception as e:
      raise serializers.ValidationError(str(e))
    else:
      serializer=StoreSerializer(data={
        "user":self.user.id,
        "title":shopifyStore.title,
        "url":shopifyStore.url,
        "hostname":shopifyStore.hostname
      })
      if serializer.is_valid():
        data=serializer.validated_data

    try:
      store=self.user.stores.get(url=data["url"])
    except Store.DoesNotExist:
      store=None
    
    if store:
      raise serializers.ValidationError(f"The store {data['url']} is already being tracked")
      
    return data

  def create(self, validated_data):
    w=WinningHunt()
    data = w.addTrackingSite(validated_data["url"])
    
    store=Store.objects.create(**validated_data)
    userStores=self.user.stores.all()
    
    name = store.hostname.split(".")[1] if store.hostname.split(".")[0] == "www" else store.hostname.split(".")[0]
    addedSites=filter(lambda x: name in x["store"],data)
    
    filteredSites=[]
    for shop in userStores:
      name = shop.hostname.split(".")[1] if shop.hostname.split(".")[0] == "www" else shop.hostname.split(".")[0]
      fd=filter(lambda x: name in x["store"],data)
      filteredSites.extend(fd)
      
    return filteredSites, addedSites, store

class AddTrackingSiteSerializer(serializers.Serializer):
  url=serializers.URLField()
  