from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from sales_tracker.models import Store
from sales_tracker.serializers import StoreSerializer, StoreAddSerializer, AddTrackingSiteSerializer, TrackDataSerializer
from drf_spectacular.utils import extend_schema, inline_serializer
from ScraperSDK.winninghunt import WinningHunt
from ApiSDK.sales_tracker import SalesTracker
from oauth2_provider.contrib.rest_framework.permissions import TokenHasReadWriteScope

# Create your views here.
class StoreViewSet(ViewSet):
  serializer_class=StoreSerializer
  permission_classes=[TokenHasReadWriteScope]

  def list(self,request):
    stores=request.user.stores.all() if request.user else Store.objects.all()
    serializer=self.serializer_class(instance=stores,many=True)
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

class TrackDataViewSet(ViewSet):
  serializer_class=TrackDataSerializer
  permission_classes=[TokenHasReadWriteScope]
  
  @extend_schema(
    responses={
      201:StoreSerializer(many=False)
    }
  )
  def create(self,request):
    serializer=self.serializer_class(data=request.data)
    if serializer.is_valid():
      trackData=serializer.save()
      return Response(data=StoreSerializer(instance=trackData.store).data,status=201)
    else:
      return Response(data=serializer.errors,status=400)