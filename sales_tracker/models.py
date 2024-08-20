from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ShopifyStore(models.Model):
  title=models.CharField(max_length=200)
  url=models.URLField(unique=True)
  hostname=models.CharField(max_length=200)
  themedata=models.JSONField()
  shopify_url=models.CharField(max_length=200)
  locale=models.CharField(max_length=200)
  currency=models.JSONField()
  
  def __str__(self):
      return self.title

class UserShopifyStore(models.Model):
  user=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='my_stores')
  store=models.ForeignKey(to=ShopifyStore,on_delete=models.CASCADE,related_name='user_stores')
  access_token=models.CharField(max_length=255,null=True)
  
  def __str__(self):
      return self.store.title
  

class UserTrackedStore(models.Model):
  user=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='tracked_stores')
  store=models.ForeignKey(to=ShopifyStore,on_delete=models.CASCADE,related_name='tracked_stores')
  
  def __str__(self):
      return self.store.title
  
  
# deprecated
class Store(models.Model):
  user=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='stores')
  title=models.CharField(max_length=200)
  url=models.URLField()
  hostname=models.CharField(max_length=200)
  themedata=models.JSONField()
  shopify_url=models.CharField(max_length=200)
  locale=models.CharField(max_length=200)
  currency=models.JSONField()
  

  def __str__(self) -> str:
    return self.title

class TrackData(models.Model):
  store=models.OneToOneField(to=Store,on_delete=models.CASCADE,related_name="track_data")
  data=models.JSONField()
  
  def __str__(self):
      return self.store.hostname
  