from rest_framework.routers import DefaultRouter
from . import views

scraperRouter = DefaultRouter()
scraperRouter.register(r'facebook-ads',views.FacebookAdsViewset,basename='facebook-ads')
scraperRouter.register(r'tiktok-ads',views.TikTokAdsViewset,basename='tiktok-ads')
scraperRouter.register(r'meta-advertisers',views.MetaAdvertisersViewset,basename='meta-advertisers')
scraperRouter.register(r'magic-ai',views.MagicAIViewSet,basename="magic-ai")
scraperRouter.register(r'save-ad',views.SaveAdViewSet,basename='save-ad')