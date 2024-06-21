from rest_framework import viewsets
from rest_framework.response import Response
from ApiSDK.tiktok import TiktokAPI
from ApiSDK.facebook import FacebookAPI
from ScraperSDK.winninghunt import WinningHunt
from django.contrib.auth.models import User
from scraper.models import (
  SavedAd
)
from scraper.serializers import (
  SavedAdSerializer
)

# Create your views here.
class FacebookAdsViewset(viewsets.ViewSet):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    
  def list(self,request):
    facebook = FacebookAPI()
    search_term = request.GET.get("search_term",None)
    country = request.GET.get("country",None)
    if search_term:
      if country:
        response = facebook.getAds(search_term=search_term,country=country)
      else:
        response = facebook.getAds(search_term=search_term)
      return Response(response)
    else:
      return Response({
        "error":"search_term is required!"
      })

class MetaAdvertisersViewset(viewsets.ViewSet):
  def list(self,request):
    w = WinningHunt()
    data = w.moveToMetaAdvertisers()
    return Response(data)

class TikTokAdsViewset(viewsets.ViewSet):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
  
  def list(self,request):
    tiktok = TiktokAPI()
    search_term = request.GET.get("search_term",None)
    if search_term:
      response = tiktok.getAds(search_term=search_term)
      return Response(response)
    else:
      return Response({
        "error":"search_term is required!"
      })
  
  def retrieve(self,request,pk):
    tiktok = TiktokAPI()
    response = tiktok.getAd(pk)
    return Response(response)

class MagicAIViewSet(viewsets.ViewSet):
  def list(self,request):
    tiktok = TiktokAPI()
    facebook = FacebookAPI()
    search_term = request.GET.get("search_term",None)
    if search_term:
      tiktokAdsData = tiktok.getAds(search_term=search_term)
      facebookAdsData = facebook.getAds(search_term=search_term)
      return Response({
        "facebok":facebookAdsData,
        "tiktok":tiktokAdsData
      })
    else:
      return Response({
        "error":"search_term is required!"
      })

class SaveAdViewSet(viewsets.ViewSet):
  def list(self,request):
    username=request.query_params.get('username')
    if username:
      user=User.objects.get(username=username)
      savedAds = SavedAd.objects.filter(user=user)
      serializer=SavedAdSerializer(savedAds,many=True)
      return Response(data=serializer.data)
    else:
      return Response({
        "errors":["username is required"]
      })
    
  def create(self,request):
    serializer = SavedAdSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(data=serializer.data,status=201)
    
    return Response(data=serializer.errors)