from django.db import models
from django.contrib.auth.models import User
from sales_tracker.models import ShopifyStore
from ScraperSDK import shopify
import logging

logger = logging.getLogger(__file__)

# Create your models here.
class AdCountry(models.Model):
  code=models.CharField(max_length=200,unique=True)
  
  def __str__(self):
    return self.code
  
class FacebookPage(models.Model):
  page_id=models.BigIntegerField(unique=True)
  name=models.CharField(max_length=200)
  profile_picture_url=models.URLField()
  page_url=models.URLField(null=True)
  likes=models.IntegerField(default=0)
  ig_username=models.CharField(max_length=200,null=True)
  ig_followers=models.IntegerField(default=0)
  
  def __str__(self):
    return str(self.name)

class FacebookCreative(models.Model):
  creative_id=models.BigIntegerField(unique=True)
  
  def __str__(self):
    return str(self.creative_id)
  
facebook_ad_display_format_choices=(
  ('image','Image'),
  ('video','Video'),
  ('carousel','Carousel'),
  ('dco','DCO'),
)
class FacebookAd(models.Model):
  page=models.ForeignKey(to=FacebookPage,on_delete=models.CASCADE,related_name='ads')
  ad_archive_id=models.BigIntegerField(unique=True)
  ad_creative=models.ForeignKey(to=FacebookCreative,on_delete=models.CASCADE,related_name='ads')
  display_format=models.CharField(max_length=200,choices=facebook_ad_display_format_choices)
  link_url=models.URLField(null=True)
  image=models.URLField(null=True)
  video=models.URLField(null=True)
  video_preview=models.URLField(null=True)
  creation_time=models.DateTimeField()
  start_date=models.DateTimeField()
  end_date=models.DateTimeField()
  body_html=models.TextField()
  caption=models.CharField(max_length=200,null=True)
  cta_text=models.CharField(max_length=200,null=True)
  country=models.ForeignKey(to=AdCountry,on_delete=models.CASCADE,related_name='ads')
  shopifyStore=models.ForeignKey(to=ShopifyStore,on_delete=models.CASCADE,related_name="facebook_ads",null=True)
  
  @property
  def shopifyProduct(self):
    if self.shopifyStore:
      try:
        product=shopify.ShopifyProduct(self.link_url)
      except Exception as e:
        logger.error(e)
        return None
      else:
        return product.data
    else:
      return None
  
  def __str__(self):
    return str(self.ad_archive_id)

class SavedFacebookAd(models.Model):
  user=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name="saved_facebook_ads")
  ad=models.ForeignKey(to=FacebookAd,on_delete=models.CASCADE,related_name="saved_facebook_ads")
  
  def __str__(self):
      return self.ad.ad_archive_id
  