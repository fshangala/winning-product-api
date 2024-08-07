from rest_framework import serializers
from ApiSDK.meta_ad_library import MetaAdLibrary
from facebook_ads.models import (
  facebook_ad_display_format_choices,
  FacebookAd
)
import threading
from ApiSDK import load_facebook_ads
from django.db.models import Q

search_keyword_in_choices=(
  ('All','All'),
  ('adtext','Ad Text'),
  ('pagename','Page Name'),
)
class FacebookAdSearchSerializer(serializers.Serializer):
  search_term=serializers.CharField(required=False,default="dress",initial="dress")
  country_code=serializers.CharField(required=False,default="FR",initial="FR")
  search_keyword_in=serializers.ChoiceField(choices=search_keyword_in_choices,required=False,default="All",initial="All")
  
  def retrieve(self):
    t=threading.Thread(
      target=load_facebook_ads.search_ads,
      name="search-ads",
      daemon=True,
      args=(self.validated_data['search_term'],self.validated_data['country_code'])
    )
    t.start()
    
    ads = FacebookAd.objects.all()
    
    if self.validated_data['search_keyword_in'] == 'adtext':
      ads=ads.filter(Q(body_html__contains=self.validated_data['search_term']))
    elif self.validated_data['search_keyword_in'] == 'pagename':
      ads=ads.filter(Q(page__name__contains=self.validated_data['search_term']))
    elif self.validated_data['search_keyword_in'] == 'All':
      ads=ads.filter(Q(page__name__contains=self.validated_data['search_term']) | Q(body_html__contains=self.validated_data['search_term']))
    
    if self.validated_data['country_code'] != 'ALL':
      ads = ads.filter(country__code=self.validated_data['country_code'])
      
    return ads

class FacebookAdCountrySerializer(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  code=serializers.CharField(default="ALL",initial="ALL")

class FacebookPageSerializer(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  page_id=serializers.IntegerField()
  page_url=serializers.URLField()
  name=serializers.CharField()
  likes=serializers.IntegerField(default=0,initial=0)
  profile_picture_url=serializers.URLField()
  ig_username=serializers.CharField(required=False)
  ig_followers=serializers.IntegerField(required=False,default=0,initial=0)

class FacebookAdSerializer(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  page=FacebookPageSerializer(read_only=True,many=False)
  ad_archive_id=serializers.IntegerField()
  ad_creative_id=serializers.IntegerField()
  display_format=serializers.ChoiceField(choices=facebook_ad_display_format_choices)
  link_url=serializers.URLField(required=False)
  image=serializers.URLField()
  video=serializers.URLField()
  video_preview=serializers.URLField()
  creation_time=serializers.DateTimeField()
  start_date=serializers.DateTimeField()
  end_date=serializers.DateTimeField()
  body_html=serializers.CharField()
  caption=serializers.CharField(required=False)
  cta_text=serializers.CharField()
  country=FacebookAdCountrySerializer()