from rest_framework.routers import DefaultRouter
from facebook_ads.views import FacebookAdsViewSet

facebookAdsRouter=DefaultRouter()
facebookAdsRouter.register(r"facebook-ads/search",viewset=FacebookAdsViewSet,basename="search-facebook-ads")