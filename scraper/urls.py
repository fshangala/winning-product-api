from rest_framework.routers import DefaultRouter
from . import views

scraperRouter = DefaultRouter()
scraperRouter.register(r'facebook-ads',views.FacebookAdsViewset,basename='facebook-ads')