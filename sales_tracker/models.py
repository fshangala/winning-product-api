from django.db import models

# Create your models here.
class Store(models.Model):
  name=models.CharField(max_length=200)
  url=models.URLField()
  title=models.CharField(max_length=200,null=True)
  store_type=models.CharField(max_length=200,null=True)
  description=models.TextField(null=True)

  def __str__(self) -> str:
    return self.name