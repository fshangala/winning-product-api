from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import facebook

# Create your views here.
class FacebookAdsViewset(viewsets.ViewSet):
  def list(self,request):
    ads = facebook.fetch()
    return Response(ads)