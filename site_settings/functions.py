from site_settings.models import SiteSettings

def getSiteSettings()->SiteSettings:
  """Get site settings object

  Returns:
      SiteSettings: site settings object
  """
  siteSettings=SiteSettings.objects.first()
  if siteSettings:
    return siteSettings
  else:
    siteSettings=SiteSettings.objects.create()
    return siteSettings