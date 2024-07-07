from django.db import models

# Create your models here.
class Store(models.Model):
  title=models.CharField(max_length=200)
  url=models.URLField()
  hostname=models.CharField(max_length=200,null=True)

  def __str__(self) -> str:
    return self.title