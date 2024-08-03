from django.db import models

# Create your models here.
class FacebookAd(models.Model):
  ad_archive_id=models.CharField(max_length=200)