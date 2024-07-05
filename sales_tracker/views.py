from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from sales_tracker.models import Store
from sales_tracker.serializers import StoreSerializer, StoreAddSerializer, AddTrackingSiteSerializer
from drf_spectacular.utils import extend_schema
from ScraperSDK.winninghunt import WinningHunt

# Create your views here.
class StoreViewSet(ViewSet):
  serializer_class=StoreSerializer

  def list(self,request):
    stores=Store.objects.all()
    serializer=self.serializer_class(instance=stores,many=True)
    return Response(serializer.data)
  
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

class TrackingStoreViewSet(ViewSet):
  serializer_class=AddTrackingSiteSerializer
  
  def list(self,request):
    winningHunt=WinningHunt()
    data = winningHunt.getTrackingSites()
    return Response(data)
  
  def create(self,request):
    serializer=AddTrackingSiteSerializer(data=request.data)
    if serializer.is_valid():
      winningHunt=WinningHunt()
      data = winningHunt.addTrackingSite(url=serializer.validated_data["store_url"])
      return Response(data)
    else:
      return Response(serializer.errors)
      