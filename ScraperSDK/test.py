from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from enum import Enum
from bs4 import BeautifulSoup
import time
import os
from supabase import create_client, Client
import json
import queue, threading

class ActiveStatus(Enum):
  ALL="all"

class WinningHunt:
  def __init__(self):
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--disable-gpu')

    self.driver = webdriver.Chrome(options=options)

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
  
  def fetch(self):
    """
    Fetch ads page source
    """
    self.driver.get(f"https://winninghunter.com/pages")
  
  def login(self):
    email = self.driver.find_element(By.NAME, "Email")
    email.send_keys("malaky31@hotmail.fr")
    password = self.driver.find_element(By.NAME, "Password")
    password.send_keys("12345678")
    button = self.driver.find_element(By.CSS_SELECTOR, 'button.login')
    button.click()

w = WinningHunt()
w.fetch()
w.login()
while True:
  pass