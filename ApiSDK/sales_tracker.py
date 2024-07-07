import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class ShopifyStore:
  def __init__(self,url:str,title:str):
    assert url != "" and title != ""
    urlp=urlparse(url)
    assert urlp.hostname != None
    self.url=urlp.geturl()
    self.title=title
    self.hostname=urlp.hostname


class SalesTracker:
  def __init__(self):
    pass

  def getStoreData(self,storeUrl)->ShopifyStore:
    response = requests.get(storeUrl)
    soup = BeautifulSoup(response.text, 'html.parser')
    urlElement=soup.select("link[rel='canonical']")
    titleElement=soup.select("title")
    
    store=ShopifyStore(
      url=urlElement[0]["href"],
      title=titleElement[0].text,
    )
    return store