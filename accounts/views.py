from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from accounts.serializers import UserSerializer, GoogleLoginSerializer
from accounts.models import Profile
from oauth2_provider.views import TokenView
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers
from oauth2_provider.models import Application, AccessToken, RefreshToken
from django.utils import timezone
from oauthlib import common

# Create your views here.
class OAuthTokenView(TokenView,APIView):
  authentication_classes=[]
  permission_classes=[]
  @extend_schema(
    request=inline_serializer(
      name="InlineTokenSerializer",
      fields={
        "client_id":serializers.CharField(),
        "client_secret":serializers.CharField(),
        "grant_type":serializers.ChoiceField(choices=(('password','password'),('client_credentials','client_credentials'))),
        "username":serializers.CharField(required=True),
        "password":serializers.CharField(required=True)
      }
    ),
    responses={
      200:inline_serializer(
        name="InlineTokenResponse",
        fields={
          "access_token":serializers.CharField(),
          "expires_in":serializers.IntegerField(),
          "token_type":serializers.CharField(),
          "scope":serializers.CharField(),
          "refresh_token":serializers.CharField()
        }
      )
    }
  )
  def post(self,request,*args,**kwargs):
    return super().post(request,*args,**kwargs)

class LoginWithGoogleViewSet(ViewSet):
  serializer_class=GoogleLoginSerializer
  permission_classes=[]
  authentication_classes=[]
  
  @extend_schema(
    responses={
      200:inline_serializer(
        name="InlineTokenResponse",
        fields={
          "access_token":serializers.CharField(),
          "expires_in":serializers.IntegerField(),
          "token_type":serializers.CharField(),
          "scope":serializers.CharField(),
          "refresh_token":serializers.CharField()
        }
      )
    }
  )
  def create(self,request):
    serializer=self.serializer_class(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      
      application=Application.objects.get(client_id=serializer.validated_data["client_id"])
      access_token=AccessToken.objects.create(
        user=user,
        scope="read write group",
        expires=timezone.now()+timezone.timedelta(seconds=36000),
        token=common.generate_token(),
        application=application
      )
      refresh_token=RefreshToken.objects.create(
        user=user,
        token=common.generate_token(),
        application=application,
        access_token=access_token
      )
      return Response(data={
        "access_token":access_token.token,
        "expires_in":36000,
        "token_type":"Bearer",
        "scope":access_token.scope,
        "refresh_token":refresh_token.token
      })
    else:
      return Response(data=serializer.errors)

class MeViewSet(ViewSet):
  serializer_class=UserSerializer
  
  def list(self,request):
    serializer=self.serializer_class(instance=request.user,many=False)
    return Response(serializer.data)

class CreateAccount(ViewSet):
  """Sign up"""
  authentication_classes=[]
  permission_classes=[]
  serializer_class=UserSerializer
  def create(self,request):
    serializer=self.serializer_class(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      return Response(data=self.serializer_class(instance=user).data)
    else:
      return Response(data=serializer.errors,status=400)