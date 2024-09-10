from urllib.parse import urlparse
from websites.website_detector import WebsiteDetector

url="https://norvure.com/products/freshlock%E2%84%A2-mason-jar-vacuum-sealer"

wd=WebsiteDetector(url=url)
site=wd.detect()
print(site.name)