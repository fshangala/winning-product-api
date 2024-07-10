from rest_framework import serializers
from sales_tracker.models import Store, TrackData
from ApiSDK.sales_tracker import SalesTracker
from ScraperSDK.winninghunt import WinningHunt
from django.contrib.auth.models import User

class TrackDataSerializer(serializers.Serializer):
  store=serializers.PrimaryKeyRelatedField(queryset=Store.objects.all())
  data=serializers.JSONField()
  
  def create(self, validated_data):
    trackData = validated_data["store"].track_data
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
      raise serializers.ValidationError(f"Invalid store, please make sure the provided url is of a shopify store: {str(e)}")
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
    store=Store.objects.create(**validated_data)      
    return store

class AddTrackingSiteSerializer(serializers.Serializer):
  url=serializers.URLField()
  