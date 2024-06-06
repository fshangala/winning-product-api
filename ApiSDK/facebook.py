import os
import requests

class FacebookAd:
  """
  Retrieves an ad page content from a particular ad_url
  
  Parameters:
    ad_url (str): The ad page url
  """

  def __init__(self,ad_url):
    responseContent=requests.get(ad_url)
    self.tokens=str(responseContent.content).split('"')
  
  def getAttribute(self,attribute):
    """
    Extracts an attribute from the ad page

    Returns:
      str|None: The ad attribute value
    """
    try:
      index=self.tokens.index(attribute)
    except ValueError as e:
      return None
    else:
      return self.tokens[index+2]

class FacebookAPI:
  """
  Class to interact with the Facebook Ads API.
  """

  def __init__(self) -> None:
    self.access_key = None
    self.ads_api_endpoint = "https://graph.facebook.com/v19.0/ads_archive?fields=id,ad_snapshot_url,ad_creation_time,ad_creative_bodies,ad_creative_link_captions,ad_creative_link_descriptions,ad_creative_link_titles,ad_delivery_start_time,ad_delivery_stop_timeage_country_gender_reach_breakdown,beneficiary_payers,bylines,currency,delivery_by_region,demographic_distribution,estimated_audience_size,eu_total_reach,impressions,languages,page_id,page_name,publisher_platforms,spend,target_ages,target_gender,target_locations"

  def get_access_key(self) -> str:
    """
    Method to get the access key.

    Returns:
      str: The access key.
    """

    self.access_key = os.getenv("FACEBOOK_ACCESS_KEY")

    return self.access_key
  
  def unslash(self,value:str):
    """
    Unslashes a value
    
    Returns:
      str: Unslashed value
    """
    overslashed=value
    slashedIterable=overslashed.split("\\")
    slashed="".join(slashedIterable)
    return slashed

  def getAds(self, search_term: str, country: str = "US") -> dict:
    """ 
    Queries ads from facebook api
    Returns:
      dict: ads response
    """
    token_key = self.get_access_key()
    if token_key is None:
      return token_key

    params = {
      "ad_reached_countries": [country],
      "search_terms": search_term,
      # "limit": 1,
      "access_token": token_key
    }

    response = requests.get(self.ads_api_endpoint, params=params)
    responseData = response.json()
    for ad in responseData['data']:
      facebookAd = FacebookAd(ad['ad_snapshot_url'])

      display_format=facebookAd.getAttribute('display_format')
      ad['display_format']=display_format

      title=facebookAd.getAttribute('title')
      ad['title']=self.unslash(title)

      ad['body']=facebookAd.getAttribute('body')

      ad['page_name']=facebookAd.getAttribute('page_name')

      page_profile_picture_url=facebookAd.getAttribute('page_profile_picture_url')
      ad['page_profile_picture_url']=self.unslash(page_profile_picture_url)

      video_url=facebookAd.getAttribute('video_sd_url')
      if video_url:
        ad['video_url']=self.unslash(video_url)
      
      original_image_url=facebookAd.getAttribute('original_image_url')
      if original_image_url:
        ad['original_image_url']=self.unslash(original_image_url)

    return responseData