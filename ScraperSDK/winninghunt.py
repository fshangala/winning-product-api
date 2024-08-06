from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TimeoutError(Exception):
  def __init__(self, message:str, *args: object) -> None:
    super().__init__(*args)
    self.message=message
    
  def __str__(self) -> str:
    return self.message
  
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
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')

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
      data = self.driver.execute_script("var table = document.querySelector(\"#store-table\");var data=[];for(var i=1;i<table.rows.length;i++){var row={};for(var j=0;j<table.rows[i].cells.length;j++){row[table.rows[0].cells[j].innerText]=table.rows[i].cells[j].innerText;data.push(row);}};return data;")
      
    return data
  
  def addTrackingSite(self,url:str):
    self.driver.get("https://app.winninghunter.com/sales-tracker")
    data=None
    if "Login" in self.driver.title:
      self.login()
      try:
        WebDriverWait(self.driver,10).until(expected_conditions.title_contains("Dashboard"))
      except Exception as e:
        raise TimeoutError(message="Did not go to dashboard after login")
      data = self.addTrackingSite(url)
    elif "Sales" in self.driver.title:
      email = self.driver.find_element(By.ID, "Store-URL")
      email.send_keys(url)
      startButton=self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']")
      startButton.click()
      try:
        WebDriverWait(self.driver,10).until(expected_conditions.title_contains("Details"))
      except Exception as e:
        pass
      data = self.getTrackingSites()
    
    return data
  
  def getTrackingSites(self):
    self.driver.get("https://app.winninghunter.com/sales-tracker")
    data=None
    if "Login" in self.driver.title:
      self.login()
      try:
        WebDriverWait(self.driver,10).until(expected_conditions.title_contains("Dashboard"))
      except Exception as e:
        raise TimeoutError(message="Did not go to dashboard after login")
      data = self.getTrackingSites()
    elif "Sales" in self.driver.title:
      try:
        WebDriverWait(self.driver,10).until(element_exists("#store-table"))
      except Exception as e:
        raise TimeoutError(message="Did not find store-table")
      data = self.driver.execute_script("""
      var table = document.querySelector("#store-table");
      var data=[];
      for(var i=1;i<table.rows.length;i++){
        var row={
          "store":table.rows[i].cells[0].innerText,
          "today":table.rows[i].cells[1].innerText,
          "yesterday":table.rows[i].cells[2].innerText,
          "7days":table.rows[i].cells[3].innerText,
          "30days":table.rows[i].cells[4].innerText
        };
        data.push(row);
      };
      return data;
      """)
    
    return data
  