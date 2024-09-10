from rest_framework import serializers
from websites.models import Website
from websites.website_detector import WebsiteDetector

class WebsiteSerializer(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  name=serializers.CharField()

class DetectWebsiteSerializer(serializers.Serializer):
  url=serializers.URLField()
  
  def validate(self,data):
    wd=WebsiteDetector(data['url'])
    site=wd.detect()
    if site:
      return {
        "name":site.name
      }
    else:
      raise serializers.ValidationError(f"{data['url']} Not recognized by registered detectors.")
  
  def create(self,validated_data):
    return Website.objects.create(**validated_data)