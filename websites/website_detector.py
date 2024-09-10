from urllib.parse import urlparse
from websites.website_detector_shopify import shopify_detector
from websites.website_detector_shoplazza import shoplazza_detector

class DetectedWebsite:
  def __init__(self,name):
    self.name=name

class WebsiteDetector:
  def __init__(self,url):
    urlp=urlparse(url)
    self.url=f"{urlp.scheme}://{urlp.hostname}{urlp.path}"
    self.detectors = [
      shopify_detector,
      shoplazza_detector,
    ]
  
  def detect(self)->DetectedWebsite:
    detected=None
    for detector in self.detectors:
      data=detector(url=self.url)
      if data:
        detected=DetectedWebsite(name=data['name'])
        break
    return detected