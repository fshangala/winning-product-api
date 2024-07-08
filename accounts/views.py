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
  
class AuthToken(ObtainAuthToken):
  def post(self,request,*args,**kwargs):
    print(request.data)
    serializer = self.serializer_class(data=request.data,context={'request': request})
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    return Response({
      'token': token.key,
      'user_id': user.pk,
      'email': user.email
    })

class CreatePassword(ViewSet):
  def create(self,request,*args,**kwargs):
    email = request.GET.get("email",None)
    if email:
      pass
    else:
      return Response({
        "email": [
          "email is required"
        ]
      },401)

class GoogleLogin(ViewSet):
  """ 
  Google login viewset
  """
  def create(self,request):
    # Collect data
    email=request.data.get("email",None)
    first_name=request.data.get("first_name",None)
    last_name=request.data.get("last_name",None)
    google_id=request.data.get("google_id",None)
    picture_url=request.data.get("picture_url",None)

    # Generate response
    response = {
      "data":{
        "data":None,
        "errors":[]
      },
      "status":200
    }

    if email and google_id:
      try:
        profile=Profile.objects.get(google_id=google_id)
      except Profile.DoesNotExist:
        try:
          user=User.objects.get(email=email)
        except User.DoesNotExist:
          user=User.objects.create(
            username=email,
            first_name=first_name,
            last_name=last_name,
            email=email,
          )
          user.profile.google_id=google_id
          user.profile.picture_url=picture_url
          user.save()
          userdata=UserSerializer(user)

          response["data"]={"data":userdata.data,"errors":[]}
          response["status"]=201
        else:
          user.profile.google_id=google_id
          user.profile.picture_url=picture_url
          user.save()
          userdata=UserSerializer(user)
          response["data"]={"data":userdata.data,"errors":[]}
          response["status"]=200
      else:
        profile.google_id=google_id
        profile.picture_url=picture_url
        profile.save()
        userdata=UserSerializer(profile.user)
        response["data"]={"data":userdata.data,"errors":[]}
        response["status"]=200
    else:
      response["data"]={"data":None,"errors":["Both email and google_id are required"]}
      response["status"]=400
  
    return Response(**response)

class GetOrCreateUserByEmail(ViewSet):
  def list(self,request,*args,**kwargs):
    email = request.GET.get("email",None)
    if email:
      try:
        user = User.objects.get(email=email)
      except User.DoesNotExist:
        firstName = request.GET.get("firstName",None)
        lastName = request.GET.get("lastName",None)
        if firstName and lastName:
          user = User.objects.create(
            username=email,
            email=email,
            first_name=firstName,
            last_name=lastName
          )
          created_password = f"{user.id}@copiwin.com"
          user.set_password(created_password)
          user.save()
          return Response({
            'token':user.auth_token.key,
            'user_id':user.id,
            'email':user.email,
            'password':created_password
          },200)
        else:
          return Response({
            "firstName": [
              "firstName is required"
            ],
            "lastName": [
              "lastName is required"
            ],
          },401)
      else:
        return Response({
          'token':user.auth_token.key,
          'user_id':user.id,
          'email':user.email
        },200)
    else:
      return Response({
        "email": [
          "email is required"
        ]
      },401)

class GetUserByEmail(ViewSet):
  def list(self,request,*args,**kwargs):
    email = request.GET.get("email",None)
    print(email)
    if email:
      user = User.objects.get(email=email)
      return Response({
        'token':user.auth_token.key,
        'user_id':user.id,
        'email':user.email
      })
    else:
      return Response({
        "email": [
          "email is required"
        ]
      },401)

class CreateAccount(ViewSet):
  def create(self,request):
    if request.data.get("email",None) and request.data.get("password",None):
      user = User.objects.create(
        username=request.data["email"],
        email=request.data["email"]
      )
      user.set_password(request.data["password"])
      user.save()
      return Response({
        'token':user.auth_token.key,
        'user_id':user.id,
        'email':user.email
      })
    else:
      return Response({
        "non_field_errors": [
          "Make sure you provide both email and password for user account creation"
        ]
      })