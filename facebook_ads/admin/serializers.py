from rest_framework import serializers
from ApiSDK.load_facebook_ads import save_ads

class LoadFacebookAdsSerializer(serializers.Serializer):
  ads_data=serializers.JSONField()
  
  def create(self,validated_data):
    save_ads(validated_data["ads_data"])
    return validated_data
  
class RetrieveFacebookAdsSerializer(serializers.Serializer):
    pass