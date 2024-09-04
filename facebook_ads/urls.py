from rest_framework.routers import DefaultRouter
from facebook_ads.views import FacebookAdsViewSet, SavedFacebookAdViewSet, LoadFacebookAdsViewSet

facebookAdsRouter=DefaultRouter()
facebookAdsRouter.register(r"facebook-ads/search",viewset=FacebookAdsViewSet,basename="search-facebook-ads")
facebookAdsRouter.register(r"facebook-ads/saved-facebook-ads",viewset=SavedFacebookAdViewSet,basename="saved-facebook-ads")
facebookAdsRouter.register(r"facebook-ads/load-facebook-ads",viewset=LoadFacebookAdsViewSet,basename="load-facebook-ads")