from rest_framework.viewsets import ViewSet
from site_settings.serializers import SiteSettingsSerializer
from rest_framework.response import Response
from site_settings.models import SiteSettings

class SiteSettingsViewSet(ViewSet):
  serializer_class=SiteSettingsSerializer
  permission_classes=[]
  def list(self,request):
    site_settings=SiteSettings.objects.first()
    serializer=self.serializer_class(instance=site_settings)
    return Response(data=serializer.data)