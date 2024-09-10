from rest_framework.viewsets import ViewSet
from websites.serializers import DetectWebsiteSerializer
from rest_framework import serializers

class DetectWebsiteViewSet(ViewSet):
  serializer_class=DetectWebsiteSerializer
  
  def create(self,request):
    serializer=self.serializer_class(data=request.data)
    if serializer.is_valid():
      serializer.save()