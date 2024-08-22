from django.core.management.base import BaseCommand, CommandError
from facebook_ads.models import FacebookAd
from sales_tracker.serializers import AddShopifyStoreByUrlSerializer
import logging
from urllib.parse import urlparse
from sales_tracker.models import ShopifyStore

logger=logging.getLogger(__file__)

class Command(BaseCommand):
  help = "loads shopify stores into the database from the downloaded ads"
  
  def handle(self,*args,**kwargs):
    ads = FacebookAd.objects.all()
    for ad in ads:
      if ad.cta_text == "Shop now":
        urlp = urlparse(url=ad.link_url)
        try:
          store=ShopifyStore.objects.get(hostname=urlp.hostname)
        except ShopifyStore.DoesNotExist:
          serializer=AddShopifyStoreByUrlSerializer(data={"url":ad.link_url})
          if serializer.is_valid():
            store=serializer.save()
            ad.shopifyStore=store
            ad.save()
          else:
            logger.warning(serializer.errors)
        else:
          ad.shopifyStore=store
          ad.save()
          