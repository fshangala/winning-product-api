import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

class Shopify:
  def __init__(self,url) -> None:
    response = requests.get(url)
    lines = response.text.splitlines()
    themeDataList = list(filter(lambda x: x.startswith("Shopify.theme"),lines))
    if len(themeDataList) > 0:
      self.themeData = themeDataList[0].split("=")[1]
      self.themeData = self.themeData.split(";")[0]
      self.themeData = json.loads(self.themeData)
    else:
      raise Exception(f"{url} does not appear to be a shopify store")
    
    self.shopify_url = list(filter(lambda x: x.startswith("Shopify.shop"),lines))[0]
    self.shopify_url = self.shopify_url.split("=")[1]
    self.shopify_url = self.shopify_url.split(";")[0]
    self.shopify_url = re.sub(" +","",self.shopify_url)
    self.shopify_url = str(re.sub("\"","",self.shopify_url))
    
    self.locale = list(filter(lambda x: x.startswith("Shopify.locale"),lines))[0]
    self.locale = re.sub("Shopify.locale.*=","",self.locale)
    self.locale = re.sub("\"","",self.locale)
    self.locale = re.sub(";","",self.locale)
    self.locale = re.sub(" +","",self.locale)
    self.locale = str(self.locale)
    
    self.currency = list(filter(lambda x: x.startswith("Shopify.currency"),lines))[0]
    self.currency = re.sub("Shopify.currency.*=","",self.currency)
    self.currency = re.sub(";","",self.currency)
    self.currency = re.sub(" +","",self.currency)
    self.currency = json.loads(str(self.currency))
    
    urlp=urlparse(url)
    self.url=urlp.geturl()
    self.hostname=urlp.hostname

    soup = BeautifulSoup(response.text, 'html.parser')
    titleElement=soup.select("title")
    self.title=titleElement[0].text