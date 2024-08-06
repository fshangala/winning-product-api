"""
URL configuration for winning_product_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework.authtoken import views
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from scraper.urls import scraperRouter
from accounts.urls import accountsRouter
from sales_tracker.urls import salesTrackerRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from facebook_ads.urls import facebookAdsRouter
from oauth2_provider import urls as oauth2_urls

router = routers.DefaultRouter()
router.registry.extend(scraperRouter.registry)
router.registry.extend(accountsRouter.registry)
router.registry.extend(salesTrackerRouter.registry)
router.registry.extend(facebookAdsRouter.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('accounts/',include('accounts.urls', namespace='accounts')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('o/', include(oauth2_urls)),
    path('api-token-auth/', views.obtain_auth_token),
]