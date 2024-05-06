from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User

# Create your views here.
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