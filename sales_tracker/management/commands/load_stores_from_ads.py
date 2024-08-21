from django.core.management.base import BaseCommand, CommandError
from facebook_ads.models import FacebookAd
from sales_tracker.serializers import AddShopifyStoreByUrlSerializer
import logging

logger=logging.getLogger(__file__)

class Command(BaseCommand):
  help = "loads shopify stores into the database from the downloaded ads"
  
  def handle(self,*args,**kwargs):
    ads = FacebookAd.objects.all()
    for ad in ads:
      if ad.cta_text == "Shop now":
        serializer=AddShopifyStoreByUrlSerializer(data={"url":ad.link_url})
        if serializer.is_valid():
          serializer.save()
        else:
          logger.warning(serializer.errors)