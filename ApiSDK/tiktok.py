import urllib.parse
import requests

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

  def getAds(self):
    tokenResponse = self.getAccessToken()
    if tokenResponse.get("error",None):
      return tokenResponse
    
    response = requests.post(
      f"{self.api_root}/research/adlib/ad/query/",
      json={
        "filters": {
          "ad_published_date_range": {
            "min": "20240101",
            "max": "20240401"
          },
          "country": "ZM"
        },
        "search_term": "coffee"
      },
      params={
        "fields":"ad.id,ad.reach,ad.videos"
      },
      headers={
        "Content-Type":"application/json",
        "Authorization":f"Bearer {self.access_token}"
      }
    )

    return response.json()
