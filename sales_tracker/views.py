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
    stores=Store.objects.all()
    w=WinningHunt()
    data=w.getTrackingSites()
    filteredSites=[]
    for shop in stores:
      name = shop.hostname.split(".")[1] if shop.hostname.split(".")[0] == "www" else shop.hostname.split(".")[0]
      fd=filter(lambda x: name in x["store"],data)
      filteredSites.extend(fd)
    return Response(filteredSites)
  
  @extend_schema(
    request=AddTrackingSiteSerializer,
    responses={
      200: inline_serializer(
        name="InlineAddStoreSerializer",
        fields={
          "data":inline_serializer(
            name="InlineTrackedSiteSerializer",
            fields={
              "store":serializers.CharField(),
              "today":serializers.CharField(),
              "yesterday":serializers.CharField(),
              "7days":serializers.CharField(),
              "30days":serializers.CharField(),
            },
            many=True,
          ),
          "filtered":inline_serializer(
            name="InlineTrackedSiteSerializer",
            fields={
              "store":serializers.CharField(),
              "today":serializers.CharField(),
              "yesterday":serializers.CharField(),
              "7days":serializers.CharField(),
              "30days":serializers.CharField(),
            },
            many=True,
          ),
          "store":StoreSerializer()
        }
      )
    }
  )
  def create(self,request):
    serializer=StoreAddSerializer(user=request.user,data=request.data)
    if serializer.is_valid():
      data, filtered, store = serializer.save()
      return Response({
        "data":data,
        "filtered":filtered,
        "store":StoreSerializer(instance=store).data
      })
    else:
      return Response(serializer.errors)