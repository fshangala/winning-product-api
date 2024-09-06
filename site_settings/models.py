from django.db import models

# Create your models here.
class SiteSettings(models.Model):
  auto_load_facebook_ads=models.BooleanField(default=True)