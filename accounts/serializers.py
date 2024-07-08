from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import Profile
import requests
from oauth2_provider.models import Application

class ProfileSerializer(serializers.Serializer):
  user=serializers.PrimaryKeyRelatedField(read_only=True)
  google_id=serializers.CharField(required=False)
  profile_url=serializers.URLField(required=False)

class UserSerializer(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  username=serializers.CharField(required=True)
  email=serializers.EmailField(required=True)
  first_name=serializers.CharField()
  last_name=serializers.CharField()
  profile=ProfileSerializer(many=False,required=False)
  password=serializers.CharField(write_only=True,required=True)
  is_superuser=serializers.BooleanField(read_only=True)
  is_staff=serializers.BooleanField(read_only=True)
  is_active=serializers.BooleanField(read_only=True)
  last_login=serializers.DateTimeField(read_only=True)
  date_joined=serializers.DateTimeField(read_only=True)
  
  def create(self, validated_data:dict):
    profile_data=validated_data.pop("profile",None)
    password=validated_data.pop("password")
    user=User.objects.create(**validated_data)
    user.set_password(password)
    user.save()
    if profile_data:
      user.profile.google_id=profile_data.get("google_id",None)
      user.profile.profile_url=profile_data.get("profile_url",None)
      user.save()
    return user

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
      