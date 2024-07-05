from rest_framework import serializers
from sales_tracker.models import Store
from ApiSDK.sales_tracker import SalesTracker

class StoreSerializer(serializers.Serializer):
  name=serializers.CharField(required=True)
  url=serializers.URLField(required=True)
  title=serializers.CharField()
  store_type=serializers.CharField()
  description=serializers.CharField()

  def create(self, validated_data):
    store=Store.objects.create(**validated_data)
    return store

class StoreAddSerializer(serializers.Serializer):
  url=serializers.URLField()

  def validate(self, attrs):
    data=attrs
    sales_tracker=SalesTracker()
    try:
      shopifyStore = sales_tracker.getStoreData(storeUrl=attrs["url"])
    except Exception as e:
      raise serializers.ValidationError(str(e))
    else:
      serializer=StoreSerializer(data={
        "name":shopifyStore.name,
        "url":shopifyStore.url.geturl(),
        "title":shopifyStore.title,
        "store_type":shopifyStore.store_type,
        "description":shopifyStore.description,
      })
      print(shopifyStore.__dict__)
      if serializer.is_valid():
        data=serializer.data

    return data

  def create(self, validated_data):
    store=Store.objects.create(**validated_data)
    return store

class AddTrackingSiteSerializer(serializers.Serializer):
  store_url=serializers.URLField()