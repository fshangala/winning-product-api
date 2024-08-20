from django.contrib import admin
from sales_tracker import models

# Register your models here.
admin.site.register(models.Store)
admin.site.register(models.TrackData)
admin.site.register(models.UserShopifyStore)
admin.site.register(models.UserTrackedStore)
