from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from ScraperSDK.facebook import Facebook
from ApiSDK.tiktok import TiktokAPI
from ApiSDK.facebook import FacebookAPI
from django.utils import timezone
import threading

# Create your views here.
class FacebookAdsViewset(viewsets.ViewSet):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    
  def list(self,request):
    facebook = FacebookAPI()
    search_term = request.GET.get("search_term",None)
    if search_term:
      response = facebook.getAds(search_term=search_term)
      return Response(response)
    else:
      return Response({
        "error":"search_term is required!"
      })

class TikTokAdsViewset(viewsets.ViewSet):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
  
  def list(self,request):
    tiktok = TiktokAPI()
    search_term = request.GET.get("search_term",None)
    print(search_term)
    if search_term:
      response = tiktok.getAds(search_term=search_term)
      print(response)
      return Response(response)
    else:
      return Response({
        "error":"search_term is required!"
      })