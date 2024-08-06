import requests
from django.conf import settings
# from ApiSDK.meta_ad_library_pages import pagesJson
# from ApiSDK.meta_ad_library_page_details import pageDetailsJson
# from ApiSDK.meta_ad_library_page_ads import getPageAdsDict
# from ApiSDK.meta_ad_library_ads import adsJson
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
    if "results" in responseData:
      for adset in responseData["results"]:
        pageAds = self.pageAds(adset[0]["pageID"])
        for ad in adset:
          ad["pageAds"]=pageAds
    else:
      logger.warning(str(responseData))
    return responseData

  # def searchPages(self,query="apple"):
  #   queryParams={
  #     "query":query
  #   }
  #   url=f"{self.baseUrl}/search/pages"
  #   # response=requests.get(
  #   #   url=url,
  #   #   params=queryParams,
  #   #   headers=self.headers
  #   # )
  #   # responseData=response.json()
  #   responseData=json.loads(pagesJson)

  #   for page in responseData["results"]:
  #     page["details"]=self.pageDetails(page_id=page["id"])
  #     page["ads"]=self.pageAds(page_id=page["id"])
  #   return responseData

  # def pageDetails(self,page_id):
  #   queryParams={
  #     "page_id":page_id
  #   }
  #   url=f"{self.baseUrl}/page/details"
  #   # response=requests.get(
  #   #   url=url,
  #   #   params=queryParams,
  #   #   headers=self.headers
  #   # )
  #   # responseData=response.json()
  #   responseData=json.loads(pageDetailsJson)
  #   return responseData

  # def pageAds(self,page_id,country_code='US',platform='facebook,instagram',media_types='all',active_status='all'):
  #   queryParams={
  #     "page_id":page_id,
  #     "country_code":country_code,
  #     "platform":platform,
  #     "media_types":media_types,
  #     "active_status":active_status
  #   }
  #   url=f"{self.baseUrl}/page/ads"
  #   # response=requests.get(
  #   #   url=url,
  #   #   params=queryParams,
  #   #   headers=self.headers
  #   # )
  #   # responseData=response.json()
  #   responseData=getPageAdsDict()
  #   return responseData