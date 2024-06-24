import requests
from django.conf import settings

class MetaAdLibrary:
  def __init__(self):
    self.baseUrl='https://meta-ad-library.p.rapidapi.com'
  
  def getPages(self,query:str="apple"):
    url = f"{self.baseUrl}/search/pages"

    querystring = {"query":query}

    headers = {
      "x-rapidapi-key": settings.RAPID_API_KEY,
      "x-rapidapi-host": "meta-ad-library.p.rapidapi.com",
      "X-RapidAPI-Mock-Response": "200"
    }
    print(headers)

    response = requests.get(url, headers=headers, params=querystring)
    responseData = response.json()
    return responseData