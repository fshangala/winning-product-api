from rest_framework.routers import DefaultRouter
from facebook_ads.views import FacebookAdsViewSet, SavedFacebookAdViewSet
from facebook_ads.admin.views import (
  LoadFacebookAdsViewSet,
  AdminFacebookAdsViewSet,
  AdminMetaAdvertisersViewSet,
)

facebookAdsRouter=DefaultRouter()
facebookAdsRouter.register(r"facebook-ads/search",viewset=FacebookAdsViewSet,basename="search-facebook-ads")
facebookAdsRouter.register(r"facebook-ads/saved-facebook-ads",viewset=SavedFacebookAdViewSet,basename="saved-facebook-ads")

# Admin routes
facebookAdsRouter.register(r"api-admin/facebook-ads/load",viewset=LoadFacebookAdsViewSet,basename="admin-load-facebook-ads")
facebookAdsRouter.register(r"api-admin/facebook-ads",viewset=AdminFacebookAdsViewSet,basename="admin-facebook-ads")
facebookAdsRouter.register(r"api-admin/meta-advertisers",viewset=AdminMetaAdvertisersViewSet,basename="admin-meta-advertisers")