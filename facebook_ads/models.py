from django.db import models

# Create your models here.
class FacebookPage(models.Model):
  page_id=models.BigIntegerField(unique=True)
  page_url=models.URLField()
  name=models.CharField(max_length=200)
  likes=models.IntegerField()
  profile_picture_url=models.URLField()
  ig_username=models.CharField(max_length=200,null=True)
  ig_followers=models.IntegerField(default=0)
  
facebook_ad_display_format_choices=(
  ('image','Image'),
  ('video','Video'),
)
class FacebookAd(models.Model):
  page=models.ForeignKey(to=FacebookPage,on_delete=models.CASCADE,related_name='ads')
  ad_archive_id=models.BigIntegerField(unique=True)
  ad_creative_id=models.BigIntegerField(unique=True)
  display_format=models.CharField(max_length=200,choices=facebook_ad_display_format_choices)
  link_url=models.URLField()
  image=models.URLField()
  video=models.URLField()
  video_preview=models.URLField()
  creation_time=models.DateTimeField()
  start_date=models.DateTimeField()
  end_date=models.DateTimeField()
  body_html=models.TextField()
  caption=models.CharField(max_length=200)
  cta_text=models.CharField(max_length=200)
  