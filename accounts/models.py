from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  user=models.OneToOneField(to=User,on_delete=models.CASCADE,related_name="profile")
  google_id=models.CharField(max_length=200,unique=True,null=True)
  picture_url=models.URLField(null=True)