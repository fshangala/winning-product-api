import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

class ShopifyStore:
  def __init__(self,name:str,url:str,title:str,store_type:str,description:str):
    assert name != "" and name != None
    self.name=name
    urlp=urlparse(url)
    assert urlp.hostname != None
    self.url=urlp
    self.title=title
    self.store_type=store_type
    self.description=description


class SalesTracker:
  def __init__(self):
    pass

  def getStoreData(self,storeUrl)->ShopifyStore:
    response = requests.get(storeUrl)
    soup = BeautifulSoup(response.text, 'html.parser')

    site_meta = soup.find_all(lambda tag: tag.name == "meta" and tag.has_attr("property"))

    site_data = dict()
    for meta in site_meta:
      site_data[meta["property"]]=meta["content"]
    
    store=ShopifyStore(
      name=site_data.get("og:site_name"),
      url=site_data.get("og:url"),
      title=site_data.get("og:title"),
      store_type=site_data.get("og:type"),
      description=site_data.get("og:description")
    )
    return store