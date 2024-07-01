from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
  if created:
    Token.objects.create(user=instance)

class SavedAd(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='saved_ads')
  source=models.CharField(max_length=200,choices=[("facebook","Facebook"),("tiktok","Tiktok")])
  content=models.JSONField()
  
  def __str__(self):
      return f"{self.source}:{self.content.get('id')}"
  