from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from sales_tracker.models import Store
from sales_tracker.serializers import StoreSerializer, StoreAddSerializer, AddTrackingSiteSerializer
from drf_spectacular.utils import extend_schema, inline_serializer
from ScraperSDK.winninghunt import WinningHunt
from ApiSDK.sales_tracker import SalesTracker

# Create your views here.
class StoreViewSet(ViewSet):
  serializer_class=StoreSerializer

  def list(self,request):
    serializer=self.serializer_class(instance=request.user.stores.all(),many=True)
    return Response(data=serializer.data)
  
  @extend_schema(
    request=AddTrackingSiteSerializer
  )
  def create(self,request):
    serializer=StoreAddSerializer(user=request.user,data=request.data)
    if serializer.is_valid():
      store = serializer.save()
      return Response(data=StoreSerializer(instance=store).data,status=201)
    else:
      return Response(data=serializer.errors,status=400)