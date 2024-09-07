from site_settings.models import SiteSettings
from rest_framework import serializers

class SiteSettingsSerializer(serializers.Serializer):
  auto_load_facebook_ads=serializers.BooleanField(default=True,initial=True)
  
  def update(self,instance:SiteSettings,validated_data:dict):
    instance.auto_load_facebook_ads=validated_data["auto_load_facebook_ads"]
    instance.save()
    return instance