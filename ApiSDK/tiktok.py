import urllib.parse
import requests

class DateRange:
  def __init__(self,min:str, max:str):
    self.min = min
    self.max = max

class Countries:
  US="US"

class TiktokAPI:
  def __init__(self):
    self.access_token=None
    self.api_root="https://open.tiktokapis.com/v2"

  def getAccessToken(self):
    params = {
      "client_key":"awger5ovlqqj478t",
      "client_secret":"Sh0CjimiKTDSGL0cmJJqZv4dwdHljZrc",
      "grant_type":"client_credentials"
    }
    q=urllib.parse.urlencode(params)
    response = requests.post(f"{self.api_root}/oauth/token/",data=q,headers={
      "Content-Type":"application/x-www-form-urlencoded"
    })
    responseData = response.json()
    if responseData.get("access_token",None):
      self.access_token = responseData["access_token"]
    
    return responseData

  def getAds(
      self,
      search_term:str,
      country:str=Countries.US,
      ad_published_date_range:DateRange=DateRange("20240401","20240501")
    ):
    tokenResponse = self.getAccessToken()
    if tokenResponse.get("error",None):
      return tokenResponse
    
    response = requests.post(
      f"{self.api_root}/research/adlib/ad/query/",
      json={
        "filters": {
          "ad_published_date_range": {
            "min": ad_published_date_range.min,
            "max": ad_published_date_range.max
          },
          "country": country
        },
        "search_term": search_term,
        "max_count":12
      },
      params={
        "fields":"ad.id"
      },
      headers={
        "Content-Type":"application/json",
        "Authorization":f"Bearer {self.access_token}"
      }
    )

    responseData = response.json()

    for ad in responseData['data']['ads']:
      adResponse = requests.post(
        f"{self.api_root}/research/adlib/ad/detail/",
        json={
          "ad_id":ad['ad']['id']
        },
        params={
          "fields":"ad.id,ad.first_shown_date,ad.last_shown_date,ad.status,ad.status_statement,ad.videos,ad.image_urls,ad.reach,advertiser.business_id,advertiser.business_name,advertiser.paid_for_by,advertiser.follower_count,advertiser.avatar_url,advertiser.profile_url,ad_group.targeting_info"
        },
        headers={
          "Content-Type":"application/json",
          "Authorization":f"Bearer {self.access_token}"
        }
      )
      adResponseData = adResponse.json()
      if adResponseData['error']['code'] == 'ok':
        ad['ad']=adResponseData['data']['ad']
        ad['advertiser']=adResponseData['data']['advertiser']
        ad['ad_group']=adResponseData['data']['ad_group']
      else:
        print(adResponseData)
        ad['details']=None

    return responseData
  
  def getAd(self,ad_id:int):
    tokenResponse = self.getAccessToken()
    if tokenResponse.get("error",None):
      return tokenResponse
    adResponse = requests.post(
      f"{self.api_root}/research/adlib/ad/detail/",
      json={
        "ad_id":ad_id
      },
      params={
        "fields":"ad.id,ad.first_shown_date,ad.last_shown_date,ad.status,ad.status_statement,ad.videos,ad.image_urls,ad.reach,advertiser.business_id,advertiser.business_name,advertiser.paid_for_by,advertiser.follower_count,advertiser.avatar_url,advertiser.profile_url,ad_group.targeting_info"
      },
      headers={
        "Content-Type":"application/json",
        "Authorization":f"Bearer {self.access_token}"
      }
    )
    adResponseData = adResponse.json()
    return adResponseData
