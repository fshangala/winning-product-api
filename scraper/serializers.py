from rest_framework import serializers
from django.contrib.auth.models import User
from scraper.models import SavedAd

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model: User
    fields: "__all__"

class SavedAdSerializer(serializers.ModelSerializer):
  class Meta:
    model: SavedAd
    fields: "__all__"