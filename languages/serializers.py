from rest_framework import serializers

class LanguageSerializer(serializers.Serializer):
  name=serializers.CharField()
  code=serializers.CharField()