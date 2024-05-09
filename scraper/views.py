from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from ScraperSDK.facebook import Facebook
from ApiSDK.tiktok import TiktokAPI
from django.utils import timezone
import threading

# Create your views here.
class FacebookAdsViewset(viewsets.ViewSet):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    
  def fetchAds(self,session):
    facebook = Facebook()
    facebook.fetch(session=session)
    
  def list(self,request):
    session = f"{timezone.now().timestamp()}"
    threading.Thread(target=self.fetchAds,daemon=True,kwargs={"session":session}).start()
    
    return Response({"session":session})

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