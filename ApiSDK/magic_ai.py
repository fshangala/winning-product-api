from ApiSDK.facebook import FacebookAPI
from ApiSDK.tiktok import TiktokAPI

class MagicAI:
  def __init__(self):
    self.facebookApi = FacebookAPI()
    self.tiktokApi = TiktokAPI()
  
  def getAds(
    self,
    search_term
  ):
    facebookAds = self.facebookApi.getAds(search_term=search_term)
    tiktokAds = self.tiktokApi.getAds(search_term=search_term)
    return {
      "facebook":facebookAds,
      "tiktok":tiktokAds
    }