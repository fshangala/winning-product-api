from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import Profile
import requests
from oauth2_provider.models import Application, AccessToken, RefreshToken
from django.utils import timezone
from oauthlib import common

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model= Profile
    fields= "__all__"

class UserSerializer(serializers.ModelSerializer):
  profile=ProfileSerializer(many=False)
  class Meta:
    model= User
    fields= ("id","profile","last_login","is_superuser","username","first_name","last_name","email","is_staff","is_active","date_joined")

class GoogleLoginSerializer(serializers.Serializer):
  client_id=serializers.CharField(required=True)
  google_access_token=serializers.CharField(required=True)
  
  def validate(self, attrs):
    data = super().validate(attrs)
    response=requests.get(
      url=f"https://www.googleapis.com/oauth2/v1/userinfo?access_token={attrs['google_access_token']}",
      headers={
        "Authorization": f"Bearer {attrs['google_access_token']}",
        "Accept": 'application/json'
      }
    )
    application=Application.objects.get(client_id=attrs["client_id"])
    data=response.json()
    if "error" in data:
      raise serializers.ValidationError(data["error"]["message"])
    data["client_id"]=application.client_id
    return data
  
  def create(self,validated_data):
    print(validated_data)
    try:
      user=User.objects.get(email=validated_data["email"])
    except User.DoesNotExist:
      user = User.objects.create(
        username=validated_data["email"],
        email=validated_data["email"],
        first_name=validated_data["given_name"],
        last_name=validated_data["family_name"],
      )
      profile = Profile.objects.create(
        user=user,
        google_id=validated_data["id"],
        picture_url=validated_data["picture"]
      )
      user.set_password(f"{user.id}@copiwin.com")
      user.save()
    
    return user
      