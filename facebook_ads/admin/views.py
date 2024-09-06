from rest_framework.viewsets import ViewSet
from facebook_ads.admin.serializers import LoadFacebookAdsSerializer
from rest_framework.response import Response
from facebook_ads.serializers import FacebookAdSerializer, FacebookPageSerializer
from facebook_ads.models import FacebookAd, FacebookPage
from rest_framework.pagination import LimitOffsetPagination

class LoadFacebookAdsViewSet(ViewSet):
  """Loads facebook ads from json"""
  permission_classes=[]
  serializer_class=LoadFacebookAdsSerializer
  
  def create(self,request):
    serializer=self.serializer_class(data=request.data)
    if serializer.is_valid():
      response = serializer.save()
      return Response(data=response)
    else:
      return Response(data=serializer.errors,status=400)

class AdminFacebookAdsViewSet(ViewSet):
  """View facebook ads from the database"""
  permission_classes=[]
  serializer_class=FacebookAdSerializer
  pagination_class=LimitOffsetPagination
  
  def list(self,request):
    ads = FacebookAd.objects.all()
    paginator=self.pagination_class()
    results=paginator.paginate_queryset(ads,request)
    adSerializer=self.serializer_class(instance=results,many=True)
    return paginator.get_paginated_response(adSerializer.data)

class AdminMetaAdvertisersViewSet(ViewSet):
  """View meta advertisers from the database"""
  permission_classes=[]
  serializer_class=FacebookPageSerializer
  pagination_class=LimitOffsetPagination
  
  def list(self,request):
    ads = FacebookPage.objects.all()
    paginator=self.pagination_class()
    results=paginator.paginate_queryset(ads,request)
    adSerializer=self.serializer_class(instance=results,many=True)
    return paginator.get_paginated_response(adSerializer.data)
  