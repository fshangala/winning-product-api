from django.db import models

# Create your models here.
class Website(models.Model):
  name=models.CharField(max_length=200,unique=True)
  
  def __str__(self):
    return self.name
  