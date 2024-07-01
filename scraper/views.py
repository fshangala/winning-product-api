from rest_framework import viewsets
from rest_framework.response import Response
from ApiSDK.tiktok import TiktokAPI
from ApiSDK.facebook import FacebookAPI
from ScraperSDK.winninghunt import WinningHunt

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