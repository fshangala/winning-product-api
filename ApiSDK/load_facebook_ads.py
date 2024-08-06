from ApiSDK.meta_ad_library import MetaAdLibrary
from facebook_ads.models import FacebookAd, FacebookPage, FacebookCreative, AdCountry
from django.utils import timezone
import logging

logger = logging.getLogger("ApiSDK.load_facebook_ads")

def save_ad(ad:dict,country_code:str):
  try:
    ad=FacebookAd.objects.get(ad_archive_id=ad['adArchiveID'])
  except FacebookAd.DoesNotExist as e:
    try:
      page=FacebookPage.objects.get(page_id=ad["snapshot"]["page_id"])
    except FacebookPage.DoesNotExist as e:
      page=FacebookPage.objects.create(
        page_id=ad['snapshot']['page_id'],
        name=ad['snapshot']['page_name'],
        profile_picture_url=ad['snapshot']['page_profile_picture_url']
      )
    
    try:
      creative=FacebookCreative.objects.get(creative_id=int(ad['snapshot']['ad_creative_id']))
    except FacebookCreative.DoesNotExist as e:
      creative=FacebookCreative.objects.create(
        creative_id=int(ad['snapshot']['ad_creative_id'])
      )
    
    try:
      ad_country=AdCountry.objects.get(code=country_code)
    except AdCountry.DoesNotExist:
      ad_country=AdCountry.objects.create(
        code=country_code
      )
      
    adObj=FacebookAd.objects.create(
      page=page,
      ad_archive_id=ad['adArchiveID'],
      ad_creative=creative,
      display_format=ad['snapshot']['display_format'],
      link_url=ad['snapshot']['link_url'],
      creation_time=timezone.datetime.fromtimestamp(ad['snapshot']['creation_time']),
      start_date=timezone.datetime.fromtimestamp(ad['startDate']),
      end_date=timezone.datetime.fromtimestamp(ad['endDate']),
      body_html=ad['snapshot']['body']['markup']['__html'],
      caption=ad['snapshot']['caption'],
      cta_text=ad['snapshot']['cta_text'],
      country=ad_country
    )
    adObj.image=ad['snapshot']['images'][0]['original_image_url'] if len(ad['snapshot']['images']) > 0 else None
    
    if len(ad['snapshot']['videos']) > 0:
      adObj.video=ad['snapshot']['videos'][0]['video_sd_url']
      adObj.video_preview=ad['snapshot']['videos'][0]['video_preview_image_url']
    
    adObj.save()
    return adObj
  else:
    return None

def search_ads(search_term:str,country_code:str):
  meta=MetaAdLibrary()
  ads = meta.searchAds(search_term=search_term,country_code=country_code)
  
  if "results" in ads:
    for adset in ads["results"]:
      for ad in adset:
        save_ad(ad,ads['country_code'])