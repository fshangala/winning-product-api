from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, inline_serializer
from ApiSDK.meta_ad_library import MetaAdLibrary
from facebook_ads.serializers import (
  FacebookAdSearchSerializer,
  FacebookAdSerializer
)

class FacebookAdsViewSet(ViewSet):
  permission_classes=[] # TODO: This must be off
  serializer_class=FacebookAdSerializer
  
  @extend_schema(
    parameters=[FacebookAdSearchSerializer()]
  )
  def list(self,request):
    serializer=FacebookAdSearchSerializer(data=request.query_params)
    if serializer.is_valid():
      ads = serializer.retrieve()
      adSerializer=self.serializer_class(instance=ads,many=True)
      return Response(data=adSerializer.data)
    else:
      return Response(data=serializer.errors,status=400)