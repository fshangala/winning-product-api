from rest_framework import serializers
from ApiSDK.meta_ad_library import MetaAdLibrary

class FacebookAdSearchSerializer(serializers.Serializer):
  search_term=serializers.CharField(required=True)
  country_code=serializers.CharField(required=False,default="US",initial="US")
  
  def retrieve(self):
    meta=MetaAdLibrary()
    ads = meta.searchAds(search_term=self.validated_data['search_term'],country_code=self.validated_data['country_code'])
    
    return ads