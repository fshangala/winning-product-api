from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from ApiSDK.meta_ad_library import MetaAdLibrary

class FacebookAdsViewSet(ViewSet):
  def list(self,request):
    metaAdLibrary=MetaAdLibrary()
    ads = metaAdLibrary.searchAds()
    return Response(data=ads)