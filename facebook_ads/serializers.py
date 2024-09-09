from rest_framework import serializers
from ApiSDK.meta_ad_library import MetaAdLibrary
from facebook_ads.models import (
  facebook_ad_display_format_choices,
  FacebookAd,
  SavedFacebookAd
)
import threading
from ApiSDK import load_facebook_ads
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.models import User
from accounts.serializers import UserSerializer
from sales_tracker.serializers import ShopifyStoreSerializer
from websites.serializers import WebsiteSerializer
from ApiSDK.load_facebook_ads import save_ads
from site_settings.functions import getSiteSettings

search_keyword_in_choices=(
  ('All','All'),
  ('adtext','Ad Text'),
  ('pagename','Page Name'),
)
media_type_choices=(
  ('all','All'),
  ('videos','Videos'),
  ('images','Images'),
  ('carousel','Carousel'),
  ('dco','DCT/Advantage+/ASC'),
)
sort_direction_choices=(
  ('asc','Ascending'),
  ('desc','Descending'),
)
class FacebookAdSearchSerializer(serializers.Serializer):
  search_term=serializers.CharField(required=False)
  country_code=serializers.CharField(required=False)
  search_keyword_in=serializers.ChoiceField(choices=search_keyword_in_choices,required=False)
  media_type=serializers.ChoiceField(choices=media_type_choices,required=False)
  sort_direction=serializers.ChoiceField(choices=sort_direction_choices,required=False)
  ad_creation_date=serializers.CharField(required=False)
  offset=serializers.IntegerField(default=0,initial=0,required=False)
  randomize=serializers.BooleanField(required=False,default=False,initial=False)
  
  def retrieve(self):
    offset=self.validated_data.get("offset")
    search_term=self.validated_data.get('search_term')
    country_code=self.validated_data.get('country_code')
    
    siteSettings=getSiteSettings()
    if siteSettings.auto_load_facebook_ads:
      if not offset > 0 and search_term:
        t=threading.Thread(
          target=load_facebook_ads.search_ads,
          name="search-ads",
          daemon=True,
          args=(self.validated_data['search_term'],country_code)
        )
        t.start()
    
    ads = FacebookAd.objects.all()
    
    # search_keyword_in
    search_keyword_in=self.validated_data.get('search_keyword_in')
    if search_term:
      if search_keyword_in:
        if search_keyword_in == 'adtext':
          ads=ads.filter(Q(body_html__icontains=self.validated_data['search_term']))
        elif search_keyword_in == 'pagename':
          ads=ads.filter(Q(page__name__icontains=self.validated_data['search_term']))
      else:
        ads=ads.filter(Q(page__name__icontains=self.validated_data['search_term']) | Q(body_html__icontains=self.validated_data['search_term']))
    
    # country_code
    if country_code:
      countries=country_code.split(",")
      q=ads.filter(country__code=countries[0])
      if len(countries) > 1:
        for country in countries[1:]:
          q=q.union(ads.filter(country__code=country))
    
    # media_type
    media_type=self.validated_data.get('media_type')
    if media_type:
      if self.validated_data['media_type'] == 'videos':
        ads = ads.filter(video__isnull=False)
      elif self.validated_data['media_type'] == 'images':
        ads = ads.filter(image__isnull=False)
    
    # sort_direction
    sort_direction=self.validated_data.get('sort_direction')
    if sort_direction:
      if self.validated_data['sort_direction'] == 'asc':
        ads = ads.order_by("body_html")
      elif self.validated_data['sort_direction'] == 'desc':
        ads = ads.order_by("-body_html")
    
    # ad_creation_date
    ad_creation_date=self.validated_data.get('ad_creation_date')
    if ad_creation_date:
      ad_creation_date=ad_creation_date.split(' - ')
      print(ad_creation_date)
      ad_creation_date_start=timezone.datetime.strptime(ad_creation_date[0],"%d/%m/%Y")
      ad_creation_date_stop=timezone.datetime.strptime(ad_creation_date[1],"%d/%m/%Y")
      ads = ads.filter(creation_time__gte=ad_creation_date_start).filter(creation_time__lte=ad_creation_date_stop)
    
    if self.validated_data['randomize']:
      ads=ads.order_by('?')
      
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
  shopifyStore=ShopifyStoreSerializer(many=False,read_only=True)
  shopifyProduct=serializers.JSONField(read_only=True)
  website=WebsiteSerializer(many=False,read_only=True)
  
class SavedFacebookAdSerializer(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  user=UserSerializer(many=False)
  ad=FacebookAdSerializer(many=False)

class SaveFacebookAdSerializer(serializers.Serializer):
  ad_archive_id=serializers.IntegerField()
  
  def __init__(self,user:User,*args,**kwargs):
    super().__init__(*args,**kwargs)
    self.user=user
  
  def validate(self,data):
    try:
      ad = FacebookAd.objects.get(ad_archive_id=data["ad_archive_id"])
    except FacebookAd.DoesNotExist as e:
      raise serializers.ValidationError(e)
    
    try:
      self.user.saved_facebook_ads.get(ad=ad)
    except SavedFacebookAd.DoesNotExist as e:
      pass
    else:
      raise serializers.ValidationError("Ad already saved!")
    
    return data
  
  def create(self,validated_data):
    ad=FacebookAd.objects.get(ad_archive_id=validated_data["ad_archive_id"])
    saved_ad=SavedFacebookAd.objects.create(
      ad=ad,
      user=self.user
    )
    return saved_ad