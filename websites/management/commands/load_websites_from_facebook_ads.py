from django.core.management.base import BaseCommand, CommandError
from facebook_ads.models import FacebookAd
from sales_tracker.serializers import AddShopifyStoreByUrlSerializer
import logging
from urllib.parse import urlparse
from sales_tracker.models import ShopifyStore

from websites.website_detector import WebsiteDetector
from websites.models import Website

logger=logging.getLogger(__file__)

class Command(BaseCommand):
  help = "loads Websites into the database from the downloaded ads"
  
  def handle(self,*args,**kwargs):
    ads = FacebookAd.objects.all()
    for ad in ads:
      if ad.cta_text == "Shop now":
        wd=WebsiteDetector(ad.link_url)
        site=wd.detect()
        if site:
          try:
            website=Website.objects.get(name=site.name)
          except Website.DoesNotExist:
            website=Website.objects.create(
              name=site.name
            )
          ad.website=website
          ad.save()