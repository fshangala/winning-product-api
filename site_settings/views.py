from rest_framework.viewsets import ViewSet
from site_settings.serializers import SiteSettingsSerializer
from rest_framework.response import Response
from site_settings.models import SiteSettings
from site_settings.functions import getSiteSettings

class SiteSettingsViewSet(ViewSet):
  serializer_class=SiteSettingsSerializer
  permission_classes=[]
  
  def list(self,request):
    site_settings=getSiteSettings()
    serializer=self.serializer_class(instance=site_settings)
    return Response(data=serializer.data)
  
  def create(self,request):
    site_settings=getSiteSettings()
    serializer=self.serializer_class(instance=site_settings,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(data=serializer.data)
    else:
      return Response(data=serializer.errors)