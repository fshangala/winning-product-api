from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from enum import Enum
from bs4 import BeautifulSoup
import time

class ActiveStatus(Enum):
  ALL="all"

class Facebook:
  def __init__(self):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')

    self.driver = webdriver.Chrome(options=options)
    
  def adDetails(self,ad)->list:
    """
    Get ad details
    """
    a0000 = list(list(list(list(ad.children)[0].children)[0].children)[0])[0]
    return a0000

  def getAdsFromPageSource(self)->list:
    """
    Get all the ads from the page source code
    """
    soup = BeautifulSoup(self.driver.page_source, 'html.parser')
    adsContainer = soup.find("div",class_="x1dr75xp xh8yej3 x16md763")
    
    trials = 0
    while adsContainer == None:
      time.sleep(3)
      soup = BeautifulSoup(self.driver.page_source, 'html.parser')
      adsContainer = soup.find("div",class_="x1dr75xp xh8yej3 x16md763")

    ads = list(list(adsContainer.children)[0].children)
    return ads
  
  def fetch(self,active_status=ActiveStatus.ALL):
    """
    Fetch ads page source
    """
    self.driver.get(f"https://web.facebook.com/ads/library/?active_status={active_status}&ad_type=all&country=ZM&q=boots&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped&search_type=keyword_unordered&media_type=all")
    
    ads = self.getAdsFromPageSource()
    text_ads = list()
    for ad in ads:
      details = list()
      for detail in self.adDetails(ad):
        details.append(detail.text)
      text_ads.append(details)
    return text_ads