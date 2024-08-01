from rest_framework import serializers

class FacebookAdSearchSerializer(serializers.Serializer):
  search_term=serializers.CharField(required=True)