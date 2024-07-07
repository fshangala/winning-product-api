from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from sales_tracker.models import Store
from sales_tracker.serializers import StoreSerializer, StoreAddSerializer, AddTrackingSiteSerializer
from drf_spectacular.utils import extend_schema
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
    for store in stores:
      s=SalesTracker()
      shop=s.getStoreData(storeUrl=store.url)
      name = shop.hostname.split(".")[1] if shop.hostname.split(".")[0] == "www" else shop.hostname.split(".")[0]
      fd=filter(lambda x: name in x["store"],data)
      filteredSites.extend(fd)
    return Response(filteredSites)
  
  @extend_schema(
    request=StoreAddSerializer,
    responses=StoreSerializer
  )
  def create(self,request):
    serializer=StoreAddSerializer(data=request.data)
    if serializer.is_valid():
      store = serializer.save()
      return Response(StoreSerializer(instance=store).data)
    else:
      return Response(serializer.errors)