from django.contrib import admin
from facebook_ads import  models

# Register your models here.
admin.site.register(models.FacebookAd)
admin.site.register(models.FacebookPage)
admin.site.register(models.FacebookCreative)
admin.site.register(models.AdCountry)