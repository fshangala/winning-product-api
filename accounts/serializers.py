from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model= Profile
    fields= "__all__"

class UserSerializer(serializers.ModelSerializer):
  profile=ProfileSerializer(many=False)
  class Meta:
    model= User
    fields= ("id","profile","last_login","is_superuser","username","first_name","last_name","email","is_staff","is_active","date_joined")