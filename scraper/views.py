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
    response = tiktok.getAds()
    return Response(response)