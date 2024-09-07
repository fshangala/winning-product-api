from rest_framework.routers import DefaultRouter
from site_settings.views import SiteSettingsViewSet

site_settings_router=DefaultRouter()
site_settings_router.register(r"api-admin/site-settings",viewset=SiteSettingsViewSet,basename='site-settings')
