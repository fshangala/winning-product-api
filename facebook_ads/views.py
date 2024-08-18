from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import serializers
from drf_spectacular.utils import extend_schema, inline_serializer
from ApiSDK.meta_ad_library import MetaAdLibrary
from facebook_ads.serializers import (
  FacebookAdSearchSerializer,
  FacebookAdSerializer,
  SavedFacebookAdSerializer,
  SaveFacebookAdSerializer,
)
from facebook_ads.models import FacebookAd

class FacebookAdsViewSet(ViewSet):
  permission_classes=[] # TODO: This must be off
  serializer_class=FacebookAdSerializer
  pagination_class=LimitOffsetPagination
  
  @extend_schema(
    parameters=[FacebookAdSearchSerializer()]
  )
  def list(self,request):
    serializer=FacebookAdSearchSerializer(data=request.query_params)
    if serializer.is_valid():
      ads = serializer.retrieve()
      paginator=self.pagination_class()
      results=paginator.paginate_queryset(ads,request)
      adSerializer=self.serializer_class(instance=results,many=True)
      return paginator.get_paginated_response(adSerializer.data)
    else:
      return Response(data=serializer.errors,status=400)
  
  def retrieve(self,request,pk):
    facebookAd=FacebookAd.objects.get(ad_archive_id=pk)
    serializer=self.serializer_class(instance=facebookAd)
    return Response(data=serializer.data)

class SavedFacebookAdViewSet(ViewSet):
  permission_classes=[]
  serializer_class=SavedFacebookAdSerializer
  
  def list(self,request):
    serializer=self.serializer_class(instance=request.user.saved_facebook_ads.all(),many=True)
    return Response(data=serializer.data)
  
  @extend_schema(
    request=inline_serializer(
      name="InlineSaveFacebookAdSerializer",
      fields={
        "ad":serializers.PrimaryKeyRelatedField(queryset=FacebookAd.objects.all())
      }
    )
  )
  def create(self,request):
    serializer=SaveFacebookAdSerializer(user=request.user,data=request.data)
    if serializer.is_valid():
      saved_ad=serializer.save()
      return Response(data=self.serializer_class(instance=saved_ad).data)
    else:
      return Response(data=serializer.errors,status=400)
    