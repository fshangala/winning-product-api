from rest_framework import serializers

class WebsiteSerializer(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  name=serializers.CharField()