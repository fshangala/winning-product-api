from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
  
class element_exists(object):
  def __init__(self,css_selector:str):
    self.css_selector=css_selector
  
  def __call__(self,driver):
    b = driver.execute_script(f'return document.querySelector("{self.css_selector}");')
    if b:
      return b
    else:
      return False

class WinningHunt:
  def __init__(self):
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # options.add_argument('--disable-gpu')

    self.driver = webdriver.Chrome(options=options)
  
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
  
  def moveToMetaAdvertisers(self):
    self.driver.get(f"https://winninghunter.com/pages")
    data = None
    if "Login" in self.driver.title:
      self.login()
      WebDriverWait(self.driver,10).until(expected_conditions.title_contains("Dashboard"))
      data = self.moveToMetaAdvertisers()
    elif "Pages" in self.driver.title:
      WebDriverWait(self.driver,20).until(element_exists("#store-table .dt-center a"))
      data = self.driver.execute_script("""
      var table = document.querySelector("#store-table");
      var data=[];
      for(var i=1;i<table.rows.length;i++){
        var row={
          "page":{
            "url":table.rows[i].cells[0].querySelector("a").getAttribute("href"),
            "picture_url":table.rows[i].cells[0].querySelector("a img").getAttribute("src"),
            "name":table.rows[i].cells[0].querySelector("a div").innerText
          },
          "countries":Array.from(table.rows[i].cells[1].querySelectorAll("img")).map((value)=>value.getAttribute("src")),
          "website":Array.from(table.rows[i].cells[2].querySelectorAll("img")).map((value)=>value.getAttribute("src")),
          "ads":table.rows[i].cells[3].innerText,
          "adsets":table.rows[i].cells[4].innerText,
          "avgAdsets":table.rows[i].cells[5].innerText,
          "likes":table.rows[i].cells[6].innerText,
          "followers":table.rows[i].cells[7].innerText,
          "created":table.rows[i].cells[8].innerText
        };
        data.push(row);
      };
      return data;
      """)
      
    return data
    
# w = WinningHunt()
# data = w.moveToMetaAdvertisers()
# print(data)
# print(type(data))
# print(dir(data))
# while True:
#   pass