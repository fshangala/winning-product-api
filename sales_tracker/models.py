from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Store(models.Model):
  user=models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='stores')
  title=models.CharField(max_length=200)
  url=models.URLField(unique=True)
  hostname=models.CharField(max_length=200,null=True)

  def __str__(self) -> str:
    return self.title