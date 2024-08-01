from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, inline_serializer
from ApiSDK.meta_ad_library import MetaAdLibrary
from facebook_ads.serializers import FacebookAdSearchSerializer

class FacebookAdsViewSet(ViewSet):
  @extend_schema(
    parameters=FacebookAdSearchSerializer()
  )
  def list(self,request):
    serializer=FacebookAdSearchSerializer(data=request.query_params)
    if serializer.is_valid():
      metaAdLibrary=MetaAdLibrary()
      ads = metaAdLibrary.searchAds(**serializer.validated_data,country_code="US")
      return Response(data=ads)
    else:
      return Response(data=serializer.errors,status=400)