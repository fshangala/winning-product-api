from django.db import models

# Create your models here.
class FacebookPage(models.Model):
  page_id=models.BigIntegerField(unique=True)
  name=models.CharField(max_length=200)
  profile_picture_url=models.URLField()
  page_url=models.URLField(null=True)
  likes=models.IntegerField(default=0)
  ig_username=models.CharField(max_length=200,null=True)
  ig_followers=models.IntegerField(default=0)
  
  def __str__(self):
    return str(self.name)

class FacebookCreative(models.Model):
  creative_id=models.BigIntegerField(unique=True)
  
  def __str__(self):
    return str(self.creative_id)
  
facebook_ad_display_format_choices=(
  ('image','Image'),
  ('video','Video'),
  ('carousel','Carousel'),
)
class FacebookAd(models.Model):
  page=models.ForeignKey(to=FacebookPage,on_delete=models.CASCADE,related_name='ads')
  ad_archive_id=models.BigIntegerField(unique=True)
  ad_creative_id=models.ForeignKey(to=FacebookCreative,on_delete=models.CASCADE,related_name='ads')
  display_format=models.CharField(max_length=200,choices=facebook_ad_display_format_choices)
  link_url=models.URLField()
  image=models.URLField(null=True)
  video=models.URLField(null=True)
  video_preview=models.URLField(null=True)
  creation_time=models.DateTimeField()
  start_date=models.DateTimeField()
  end_date=models.DateTimeField()
  body_html=models.TextField()
  caption=models.CharField(max_length=200)
  cta_text=models.CharField(max_length=200)
  
  def __str__(self):
    return str(self.ad_archive_id)
  