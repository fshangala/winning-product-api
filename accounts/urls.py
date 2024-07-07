from django.urls import path
from accounts import views
from rest_framework.routers import DefaultRouter

accountsRouter = DefaultRouter()
accountsRouter.register(r'accounts/user-by-email',viewset=views.GetOrCreateUserByEmail,basename='user-by-email')
accountsRouter.register(r'accounts/create-account',viewset=views.CreateAccount,basename='create-account')
accountsRouter.register(r'accounts/google-login',viewset=views.GoogleLogin,basename='google-login')

app_name="accounts"
urlpatterns = [
  path('api-token-auth/', views.AuthToken.as_view()),
  path('oauth-token/',view=views.OAuthTokenView.as_view())
]