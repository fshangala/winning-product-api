import requests
from django.conf import settings
import json
import logging

logger=logging.getLogger("ApiSDK.meta_ad_library")

class MetaAdLibrary:
  def __init__(self):
    self.baseUrl='https://meta-ad-library.p.rapidapi.com'
    self.headers={
      "x-rapidapi-key": settings.RAPID_API_KEY,
      "x-rapidapi-host": "meta-ad-library.p.rapidapi.com"
    }

  def searchAds(self,search_term,country_code):
    url=f"{self.baseUrl}/search/ads"
    queryParams={
      "query":search_term,
      "country_code":country_code
    }
    response=requests.get(
      url=url,
      params=queryParams,
      headers=self.headers
    )
    responseData=response.json()
    if not "results" in responseData:
      logger.warning(str(responseData))
    return responseData
