from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from ScraperSDK.facebook import Facebook

# Create your views here.
class FacebookAdsViewset(viewsets.ViewSet):
  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.facebook=Facebook()
    
  def list(self,request):
    ads = self.facebook.fetch()
    return Response(ads)