import requests
from django.conf import settings
from ApiSDK.meta_ad_library_pages import pagesJson
from ApiSDK.meta_ad_library_page_details import pageDetailsJson
from ApiSDK.meta_ad_library_page_ads import getPageAdsDict
import json

class MetaAdLibrary:
  def __init__(self):
    self.baseUrl='https://meta-ad-library.p.rapidapi.com'
    self.headers={
      "x-rapidapi-key": settings.RAPID_API_KEY,
      "x-rapidapi-host": "meta-ad-library.p.rapidapi.com"
    }

  def searchAds(self):
    pass

  def searchPages(self,query="apple"):
    queryParams={
      "query":query
    }
    url=f"{self.baseUrl}/search/pages"
    # response=requests.get(
    #   url=url,
    #   params=queryParams,
    #   headers=self.headers
    # )
    # responseData=response.json()
    responseData=json.loads(pagesJson)

    for page in responseData["results"]:
      page["details"]=self.pageDetails(page_id=page["id"])
      page["ads"]=self.pageAds(page_id=page["id"])
    return responseData

  def pageDetails(self,page_id):
    queryParams={
      "page_id":page_id
    }
    url=f"{self.baseUrl}/page/details"
    # response=requests.get(
    #   url=url,
    #   params=queryParams,
    #   headers=self.headers
    # )
    # responseData=response.json()
    responseData=json.loads(pageDetailsJson)
    return responseData

  def pageAds(self,page_id,country_code='US',platform='facebook,instagram',media_types='all',active_status='all'):
    queryParams={
      "page_id":page_id,
      "country_code":country_code,
      "platform":platform,
      "media_types":media_types,
      "active_status":active_status
    }
    url=f"{self.baseUrl}/page/ads"
    # response=requests.get(
    #   url=url,
    #   params=queryParams,
    #   headers=self.headers
    # )
    # responseData=response.json()
    responseData=getPageAdsDict()
    return responseData
  
    # url = f"{self.baseUrl}/page/ads"
    # querystring = {
    #   "page_id":f"{page_id}",
    #   "country_code":"US",
    #   "platform":"facebook,instagram",
    #   "media_types":"all",
    #   "active_status":"all"
    # }
    # headers = {
    #   "x-rapidapi-key": settings.RAPID_API_KEY,
    #   "x-rapidapi-host": "meta-ad-library.p.rapidapi.com"
    # }

    # response = requests.get(url, headers=headers, params=querystring)
    # responseData = response.json()
    # return responseData
  
    return {
      "page_id": "434174436675167",
      "country_code": "US",
      "continuation_token": "AQHRllu9DJ4wTYmRiKuOS29Gggh5o5N2ZoPleEMVQoVg696WBEMsJoZ7KMPnsdM-QKFG",
      "platform": [
        "facebook",
        "instagram"
      ],
      "media_types": "all",
      "active_status": "all",
      "is_result_complete": False,
      "number_of_ads": 91,
      "results": [
        [
          {
            "adid": "0",
            "adArchiveID": "1125459605498654",
            "archiveTypes": [],
            "categories": [
              0
            ],
            "containsDigitallyCreatedMedia": False,
            "containsSensitiveContent": False,
            "collationCount": 4,
            "collationID": 3665274860464955,
            "currency": "",
            "endDate": 1705132800,
            "entityType": "person_profile",
            "fevInfo": None,
            "gatedType": "eligible",
            "hasUserReported": False,
            "hiddenSafetyData": False,
            "hideDataStatus": "NONE",
            "impressionsWithIndex": {
              "impressionsText": None,
              "impressionsIndex": -1
            },
            "isAAAEligible": False,
            "isActive": True,
            "isProfilePage": True,
            "pageID": "434174436675167",
            "pageInfo": None,
            "pageIsDeleted": False,
            "pageName": "Apple",
            "politicalCountries": [],
            "reachEstimate": None,
            "reportCount": None,
            "snapshot": {
              "ad_creative_id": "120204523543400150",
              "cards": [
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/416324633_1300685140570059_8210692933315961428_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=Z6mlRwwu4jIAX_AEk5E&_nc_ht=scontent-atl3-1.xx&oh=00_AfAEVxtEZ2Obwd_SFAmnifXftKh6rYm276_Zimie_fPPJg&oe=65A82C69",
                  "resized_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/417739983_1848042462322699_6311695855027552136_n.jpg?stp=dst-jpg_s600x600&_nc_cat=105&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=QbQrpF7yczYAX95TcZ_&_nc_ht=scontent-atl3-2.xx&oh=00_AfAHAkgkzJTIKVm6Rz3P4qNdVU0_7qof0io3iwKd1R_aLQ&oe=65A8B996",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwim-staf-caro-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-frm2srs-static-11ar-ban-educm-na-na-na-na-na-igcar1-04063209"
                },
                {
                  "original_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418554627_1681296929067799_7480682537458245497_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=cf0ekh4_e5AAX-RwdaN&_nc_ht=scontent-atl3-2.xx&oh=00_AfCxMM5MAI0n6G1IQ4l6vWLsyqP3tOobvFO1c_leGvEH5g&oe=65A83AF2",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418566052_1434532257132967_7591139944282599276_n.jpg?stp=dst-jpg_s600x600&_nc_cat=108&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=F3OJF_yOoowAX9H1dKA&_nc_ht=scontent-atl3-1.xx&oh=00_AfB_1D0IWVcCqhxL9XBx5BeKSpYTtr5TZuv1F8qAl5DXMw&oe=65A9F9C5",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwim-staf-caro-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-frm2srs-static-11ar-ban-educm-na-na-na-na-na-igcar2-04063119"
                },
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/417696210_753018440048913_6184579315218798635_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=CJ88yyHM0vMAX8bI0Cs&_nc_ht=scontent-atl3-1.xx&oh=00_AfCYOkfPeDN7aokMyAsg7H2T4MgIVj2sAFVCwZ8rRU5S0g&oe=65AA052B",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418933465_258557717089514_6858729654086754917_n.jpg?stp=dst-jpg_s600x600&_nc_cat=107&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=Eazq2dfObO0AX8ueRRA&_nc_ht=scontent-atl3-1.xx&oh=00_AfBpT7TbgtSiLxTzqZxVfj8FvauAUJip3NT1PLTGOKQJ5A&oe=65A99142",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwim-staf-caro-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-frm2srs-static-11ar-ban-educm-na-na-na-na-na-igcar3-04063120"
                },
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/416325191_1022593745476157_7985392899138546060_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=zZy-dMJjT-AAX8sX3_V&_nc_ht=scontent-atl3-1.xx&oh=00_AfAKDuL_BGR_vvKJcvmqEGv-7uYJ_D7hWs6s7kdF-_r9Bg&oe=65A934AC",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418551126_805627601372061_7114757484176964582_n.jpg?stp=dst-jpg_s600x600&_nc_cat=103&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=nGGgwD83f7wAX_TvVo2&_nc_ht=scontent-atl3-1.xx&oh=00_AfDlAGMWAVviL7SY6JtXlrIXkzD0YxY4g1t1zVUqwPhQLw&oe=65A9BEDE",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwim-staf-caro-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-frm2srs-static-11ar-ban-educm-na-na-na-na-na-igcar4-04063121"
                }
              ],
              "body_translations": {},
              "byline": None,
              "caption": "education.apple.com",
              "cta_text": "Learn more",
              "dynamic_item_flags": {},
              "dynamic_versions": None,
              "edited_snapshots": [],
              "effective_authorization_category": "NONE",
              "event": [],
              "extra_images": [],
              "extra_links": [],
              "extra_texts": [],
              "extra_videos": [],
              "instagram_shopping_products": [],
              "display_format": "carousel",
              "title": None,
              "link_description": None,
              "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwim-staf-caro-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-frm2srs-static-11ar-ban-educm-na-na-na-na-na-igcar1-04063209",
              "page_welcome_message": None,
              "images": [],
              "videos": [],
              "creation_time": 1704850724,
              "page_id": 434174436675167,
              "page_name": "Apple",
              "page_profile_picture_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418937398_333035019554797_4466210674109656660_n.jpg?stp=dst-jpg_s60x60&_nc_cat=106&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=UJQ36PVq4bQAX8J9tLr&_nc_oc=AQkMl3uE_OpL9Rx1v5Npa5v3xfyYzR1wEEE_ni_vJlQaBgep9Gt4ZS2UPsZZtmJMHP4&_nc_ht=scontent-atl3-1.xx&oh=00_AfCA-3IO3kJTrAazdsW36YC6mDVGqb11gQ8mDtq6Dx7saQ&oe=65A86790",
              "page_categories": {
                "2201": "Product/service"
              },
              "page_entity_type": "person_profile",
              "page_is_profile_page": False,
              "instagram_actor_name": "apple",
              "instagram_profile_pic_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418554713_891566709303847_3352628967634575828_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=_rAlSRYszFIAX9RxK_Z&_nc_ht=scontent-atl3-2.xx&oh=00_AfDGnKcY_kkCmcnoXx9wfkt62LRTFoJZgHFegOSt19-Gtg&oe=65A938F8",
              "instagram_url": "",
              "instagram_handle": "",
              "is_reshared": False,
              "version": 3,
              "body": {
                "context": {},
                "markup": {
                  "__html": "Help improve literacy skills for all learners with creative lesson ideas on iPad, and find free teaching resources in the Apple Education Community."
                },
                "callerHash": "f56557a758f1ef4e5affe711ab135709"
              },
              "brazil_tax_id": None,
              "branded_content": None,
              "current_page_name": "Apple",
              "disclaimer_label": None,
              "page_like_count": 13814619,
              "page_profile_uri": "https://facebook.com/apple",
              "page_is_deleted": False,
              "root_reshared_post": None,
              "cta_type": "LEARN_MORE",
              "additional_info": None,
              "ec_certificates": None,
              "country_iso_code": None,
              "instagram_branded_content": None
            },
            "spend": None,
            "startDate": 1704787200,
            "stateMediaRunLabel": None,
            "publisherPlatform": [
              "instagram"
            ],
            "menuItems": []
          },
          {
            "adid": "0",
            "adArchiveID": "420986293587931",
            "archiveTypes": [],
            "categories": [
              0
            ],
            "containsDigitallyCreatedMedia": False,
            "containsSensitiveContent": False,
            "collationCount": None,
            "collationID": 3665274860464955,
            "currency": "",
            "endDate": 1705132800,
            "entityType": "person_profile",
            "fevInfo": None,
            "gatedType": "eligible",
            "hasUserReported": False,
            "hiddenSafetyData": False,
            "hideDataStatus": "NONE",
            "impressionsWithIndex": {
              "impressionsText": None,
              "impressionsIndex": -1
            },
            "isAAAEligible": False,
            "isActive": True,
            "isProfilePage": True,
            "pageID": "434174436675167",
            "pageInfo": None,
            "pageIsDeleted": False,
            "pageName": "Apple",
            "politicalCountries": [],
            "reachEstimate": None,
            "reportCount": None,
            "snapshot": {
              "ad_creative_id": "120204523542800150",
              "cards": [
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418898726_1489111291948481_15160672754165966_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=hCsuTMYrf40AX-uQG-S&_nc_ht=scontent-atl3-1.xx&oh=00_AfBQo92PDiTuS1EnuLyqG7n_TfurR1T9vhZ-QWC_H-aleg&oe=65A8C287",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418851499_7017418888306297_1598479917755806428_n.jpg?stp=dst-jpg_s600x600&_nc_cat=109&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=tSldoXImv2gAX8xT9up&_nc_oc=AQkaj_luyXjxqm89TaLYwBkjgOWq48PqC3q5h4B33yt2F2bWcMMxYeXQF7TGtcpGuOk&_nc_ht=scontent-atl3-1.xx&oh=00_AfAPRi5JceybV8EdpWU1dMSJTVHc2DEIcW6FDHQ5Mh2nzQ&oe=65A9BAFC",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwfm-staf-caro-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-frm2srs-static-11ar-ban-educm-na-na-na-na-na-fbcar1-04063206"
                },
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418867400_1131697318184820_8039810858653378284_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=2LDl2DwkKW0AX8MT71f&_nc_ht=scontent-atl3-1.xx&oh=00_AfCgE6xDGSU9Re3n8DcQRd-Cy-B9pFTYAEEAN7BIPVRr5A&oe=65A87D4D",
                  "resized_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/416159970_746251404051891_2202598570283272548_n.jpg?stp=dst-jpg_s600x600&_nc_cat=111&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=PgLw5MhVokAAX9Gae2N&_nc_ht=scontent-atl3-2.xx&oh=00_AfDNLnsTXOZJQaJo0lbPsvf2KaMoKN24c6ZS1B4J8YyMBw&oe=65A8B2B8",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwfm-staf-caro-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-frm2srs-static-11ar-ban-educm-na-na-na-na-na-fbcar2-04063110"
                },
                {
                  "original_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/416162194_338693569029657_1332098520177197759_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=QWGEza0oYoIAX-XVWbZ&_nc_ht=scontent-atl3-2.xx&oh=00_AfBgUF9aixSUkNxsRoS-6_No0aa0RufvQZ-vGkbX2R3T4w&oe=65A9BB48",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418867296_887945422820128_7290353577356853160_n.jpg?stp=dst-jpg_s600x600&_nc_cat=106&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=tPORkYdt5GMAX-8gAvy&_nc_ht=scontent-atl3-1.xx&oh=00_AfACAYnju22G-hnNeQaJdAF20GAgOb518AZEd8ZSHWvO7g&oe=65A879FB",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwfm-staf-caro-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-frm2srs-static-11ar-ban-educm-na-na-na-na-na-fbcar3-04063111"
                },
                {
                  "original_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418848522_3604457126490272_8534707873131131811_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=KczsEndJr-gAX_5DlVh&_nc_ht=scontent-atl3-2.xx&oh=00_AfCBFiXfv3FXwRn4V6ey9-ZnE7G9WeGfAxs2rbH7xZZHBQ&oe=65A9F459",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418841437_903320634832442_2068285993890822972_n.jpg?stp=dst-jpg_s600x600&_nc_cat=109&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=X6dh_2JwWsAAX-1Eg-T&_nc_oc=AQm-u9d83yJGFmKhvjH1J8oWp_aVDpOO93Ed5o1eizHt2zhsmdJ_aZWjGMEei3uqfFk&_nc_ht=scontent-atl3-1.xx&oh=00_AfAwbeddCz0diTxypRhwrTL5nk4XKjPtn5qNmjUrkOu5pQ&oe=65A9CA60",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwfm-staf-caro-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-frm2srs-static-11ar-ban-educm-na-na-na-na-na-fbcar4-04063112"
                }
              ],
              "body_translations": {},
              "byline": None,
              "caption": "education.apple.com",
              "cta_text": "Learn more",
              "dynamic_item_flags": {},
              "dynamic_versions": None,
              "edited_snapshots": [],
              "effective_authorization_category": "NONE",
              "event": [],
              "extra_images": [],
              "extra_links": [],
              "extra_texts": [],
              "extra_videos": [],
              "instagram_shopping_products": [],
              "display_format": "carousel",
              "title": "Apple",
              "link_description": None,
              "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwfm-staf-caro-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-frm2srs-static-11ar-ban-educm-na-na-na-na-na-fbcar1-04063206",
              "page_welcome_message": None,
              "images": [],
              "videos": [],
              "creation_time": 1704850721,
              "page_id": 434174436675167,
              "page_name": "Apple",
              "page_profile_picture_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418895567_809301980962974_880046591914392337_n.jpg?stp=dst-jpg_s60x60&_nc_cat=104&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=xH0Cpd-oXQQAX_I4YN1&_nc_ht=scontent-atl3-2.xx&oh=00_AfDbTYlzBMqui6Zzk84up6thfx1oizwlizSfWhgwMl0UGg&oe=65A94F70",
              "page_categories": {
                "2201": "Product/service"
              },
              "page_entity_type": "person_profile",
              "page_is_profile_page": False,
              "instagram_actor_name": "",
              "instagram_profile_pic_url": "",
              "instagram_url": "",
              "instagram_handle": "",
              "is_reshared": False,
              "version": 3,
              "body": {
                "context": {},
                "markup": {
                  "__html": "Help improve literacy skills for all learners with creative lesson ideas on iPad, and find free teaching resources in the Apple Education Community."
                },
                "callerHash": "f56557a758f1ef4e5affe711ab135709"
              },
              "brazil_tax_id": None,
              "branded_content": None,
              "current_page_name": "Apple",
              "disclaimer_label": None,
              "page_like_count": 13814619,
              "page_profile_uri": "https://facebook.com/apple",
              "page_is_deleted": False,
              "root_reshared_post": None,
              "cta_type": "LEARN_MORE",
              "additional_info": None,
              "ec_certificates": None,
              "country_iso_code": None,
              "instagram_branded_content": None
            },
            "spend": None,
            "startDate": 1704787200,
            "stateMediaRunLabel": None,
            "publisherPlatform": [
              "facebook"
            ],
            "menuItems": []
          },
          {
            "adid": "0",
            "adArchiveID": "743617530624425",
            "archiveTypes": [],
            "categories": [
              0
            ],
            "containsDigitallyCreatedMedia": False,
            "containsSensitiveContent": False,
            "collationCount": None,
            "collationID": 3665274860464955,
            "currency": "",
            "endDate": 1705132800,
            "entityType": "person_profile",
            "fevInfo": None,
            "gatedType": "eligible",
            "hasUserReported": False,
            "hiddenSafetyData": False,
            "hideDataStatus": "NONE",
            "impressionsWithIndex": {
              "impressionsText": None,
              "impressionsIndex": -1
            },
            "isAAAEligible": False,
            "isActive": True,
            "isProfilePage": True,
            "pageID": "434174436675167",
            "pageInfo": None,
            "pageIsDeleted": False,
            "pageName": "Apple",
            "politicalCountries": [],
            "reachEstimate": None,
            "reportCount": None,
            "snapshot": {
              "ad_creative_id": "120204523542920150",
              "cards": [
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418554089_922258192815675_796566797777365892_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=tE3nhB9zJA8AX8p8qQ-&_nc_ht=scontent-atl3-1.xx&oh=00_AfASPhJ5e8rVehgW-qtYJYzE4gO2s0lfx7UwrpXvH3aUMA&oe=65A8B8DE",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418590094_694507076083656_6051271516326899053_n.jpg?stp=dst-jpg_s600x600&_nc_cat=107&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=hsxFwxYjtjoAX_hjFKs&_nc_ht=scontent-atl3-1.xx&oh=00_AfAAx09rMFEIc4MQwpSrjpF6Zx6lcBp_Kpdnc3M_hQrjgQ&oe=65A87A35",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwim-staf-caro-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-frm2srs-static-11ar-ban-educm-na-na-na-na-na-igcar1-04063215"
                },
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418594105_1020305745737487_7839618737209004456_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=tIbafM71DP4AX-STVMY&_nc_ht=scontent-atl3-1.xx&oh=00_AfDLfz1nPFB8DTVY0aMYKrkeBxA7KgAVXBRKG5rXG2kmyg&oe=65A8B8B5",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418539605_1107778030232992_8087942966468975952_n.jpg?stp=dst-jpg_s600x600&_nc_cat=103&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=GHwrKeODZ3YAX_nuVYM&_nc_ht=scontent-atl3-1.xx&oh=00_AfCFVYTyjz7J3MY1Z8hbD-b3UW8FwE5yY4JAU-pGVd8lTA&oe=65A9B8A6",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwim-staf-caro-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-frm2srs-static-11ar-ban-educm-na-na-na-na-na-igcar2-04063137"
                },
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418593734_7394962293871719_2004348185615830475_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=rDEj1ZW8MiUAX8kkDNF&_nc_ht=scontent-atl3-1.xx&oh=00_AfDqEs5n0M7oUoQzE5isR3fowvZgo82riKIvJ7AFdStOQA&oe=65A85C3C",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418574081_3471499639829639_6866313231986412188_n.jpg?stp=dst-jpg_s600x600&_nc_cat=109&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=U9G-W7BPmPQAX8HY0pI&_nc_ht=scontent-atl3-1.xx&oh=00_AfCZBaZnnhvRW6UoV_uX1Vm7vYmbuDCGhVX-otGdq5yB1A&oe=65A93A4F",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwim-staf-caro-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-frm2srs-static-11ar-ban-educm-na-na-na-na-na-igcar3-04063138"
                },
                {
                  "original_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418566339_331971556342730_7704155037130353026_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=72s_KRmojF8AX-aeLko&_nc_ht=scontent-atl3-2.xx&oh=00_AfBOy5T48zUqjSbMzFYEJNlZonI4kk-rEOdmWOY8eK10gQ&oe=65AA1532",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418587910_355285623876230_4968432109810057597_n.jpg?stp=dst-jpg_s600x600&_nc_cat=103&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=xGdSykr3skMAX9R_tn7&_nc_ht=scontent-atl3-1.xx&oh=00_AfDDrkeJr7SSBcdDerKQlvfVu4iCN0w3p_xCLbwYCa5Tsg&oe=65A84602",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwim-staf-caro-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-frm2srs-static-11ar-ban-educm-na-na-na-na-na-igcar4-04063139"
                }
              ],
              "body_translations": {},
              "byline": None,
              "caption": "education.apple.com",
              "cta_text": "Learn more",
              "dynamic_item_flags": {},
              "dynamic_versions": None,
              "edited_snapshots": [],
              "effective_authorization_category": "NONE",
              "event": [],
              "extra_images": [],
              "extra_links": [],
              "extra_texts": [],
              "extra_videos": [],
              "instagram_shopping_products": [],
              "display_format": "carousel",
              "title": None,
              "link_description": None,
              "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwim-staf-caro-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-frm2srs-static-11ar-ban-educm-na-na-na-na-na-igcar1-04063215",
              "page_welcome_message": None,
              "images": [],
              "videos": [],
              "creation_time": 1704850720,
              "page_id": 434174436675167,
              "page_name": "Apple",
              "page_profile_picture_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418590513_888339799411963_3645602333450651512_n.jpg?stp=dst-jpg_s60x60&_nc_cat=106&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=nZyCkikYM3EAX-f8eHu&_nc_ht=scontent-atl3-1.xx&oh=00_AfDukj9-0ZG0RE_kHri6X81g2axsuGmCIEU5NDSYntfEtQ&oe=65AA0CC9",
              "page_categories": {
                "2201": "Product/service"
              },
              "page_entity_type": "person_profile",
              "page_is_profile_page": False,
              "instagram_actor_name": "apple",
              "instagram_profile_pic_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418557498_263715466534302_5733031477022716676_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=n_YgmTckST0AX-uuv-W&_nc_ht=scontent-atl3-1.xx&oh=00_AfCHg70tOiuC_-NPYgL6moWIiQC_ypzaldWoyMFUswJmMQ&oe=65A9CABE",
              "instagram_url": "",
              "instagram_handle": "",
              "is_reshared": False,
              "version": 3,
              "body": {
                "context": {},
                "markup": {
                  "__html": "Help improve literacy skills for all learners with creative lesson ideas on iPad, and find free teaching resources in the Apple Education Community."
                },
                "callerHash": "f56557a758f1ef4e5affe711ab135709"
              },
              "brazil_tax_id": None,
              "branded_content": None,
              "current_page_name": "Apple",
              "disclaimer_label": None,
              "page_like_count": 13814619,
              "page_profile_uri": "https://facebook.com/apple",
              "page_is_deleted": False,
              "root_reshared_post": None,
              "cta_type": "LEARN_MORE",
              "additional_info": None,
              "ec_certificates": None,
              "country_iso_code": None,
              "instagram_branded_content": None
            },
            "spend": None,
            "startDate": 1704787200,
            "stateMediaRunLabel": None,
            "publisherPlatform": [
              "instagram"
            ],
            "menuItems": []
          },
          {
            "adid": "0",
            "adArchiveID": "1053486559237901",
            "archiveTypes": [],
            "categories": [
              0
            ],
            "containsDigitallyCreatedMedia": False,
            "containsSensitiveContent": False,
            "collationCount": None,
            "collationID": 3665274860464955,
            "currency": "",
            "endDate": 1705132800,
            "entityType": "person_profile",
            "fevInfo": None,
            "gatedType": "eligible",
            "hasUserReported": False,
            "hiddenSafetyData": False,
            "hideDataStatus": "NONE",
            "impressionsWithIndex": {
              "impressionsText": None,
              "impressionsIndex": -1
            },
            "isAAAEligible": False,
            "isActive": True,
            "isProfilePage": True,
            "pageID": "434174436675167",
            "pageInfo": None,
            "pageIsDeleted": False,
            "pageName": "Apple",
            "politicalCountries": [],
            "reachEstimate": None,
            "reportCount": None,
            "snapshot": {
              "ad_creative_id": "120204523542830150",
              "cards": [
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418499267_888503369600577_3359945364606149830_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=_vaM_Uo02ZgAX-Ou3tB&_nc_ht=scontent-atl3-1.xx&oh=00_AfD7DHZqSIUiRGHJ1A0ofEa012gffLA01Fc6v9YpELy20w&oe=65A99296",
                  "resized_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/416435267_6973037352808596_871720909206717215_n.jpg?stp=dst-jpg_s600x600&_nc_cat=102&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=rnG4-2y5ZjgAX_jhFzT&_nc_ht=scontent-atl3-2.xx&oh=00_AfDHdwwyf_gsNXows2vX9NlungXbGME24YilqcLULwFLVg&oe=65A8DDC3",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwfm-staf-caro-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-frm2srs-static-11ar-ban-educm-na-na-na-na-na-fbcar1-04063212"
                },
                {
                  "original_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418514415_336357765879428_5981898176375259207_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=Y6NkeuHdsJAAX8tgBaW&_nc_oc=AQle-iFhZ7wsrgRB00-dRBpK6OnylI13SzsVyXJQNzjQcTBYgZ1eavIKEkvo2jjgaKQ&_nc_ht=scontent-atl3-2.xx&oh=00_AfCoRfDLKBpJ6xyHtQIp-eLBpezo-0gInk2ueP0xNN4USg&oe=65AA1976",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/416348044_342944211920061_3036930836982483671_n.jpg?stp=dst-jpg_s600x600&_nc_cat=106&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=oBf84KXs6O8AX-zHMMd&_nc_ht=scontent-atl3-1.xx&oh=00_AfDxn4gvS3x_Nx83FP6MH-BEikkm5n5hJmKAVi1gZIzB8w&oe=65A8C8A9",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwfm-staf-caro-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-frm2srs-static-11ar-ban-educm-na-na-na-na-na-fbcar2-04063128"
                },
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/416375093_684800320484901_5847226733008082649_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=xQCf4Aaqn9QAX9r7Khj&_nc_ht=scontent-atl3-1.xx&oh=00_AfBZLwmQYfpQ8rCUzvo-jNWhZMo8Qcr1xoPJrnGGGdlBSg&oe=65A82628",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418513940_895864975878399_3223847459886706665_n.jpg?stp=dst-jpg_s600x600&_nc_cat=100&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=wMpSQjLNsVcAX-PbhcF&_nc_ht=scontent-atl3-1.xx&oh=00_AfBJ8E_mcbfvsywR278FtMTRBImLNjNUAGyw12ouRM4aiA&oe=65A9B726",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwfm-staf-caro-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-frm2srs-static-11ar-ban-educm-na-na-na-na-na-fbcar3-04063129"
                },
                {
                  "original_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418545411_7881171925232705_9159224671859453879_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=PdoFl-vbWPAAX86kzHt&_nc_ht=scontent-atl3-2.xx&oh=00_AfAKRoUsPSWdhZH5zBzxY68lS0VcmBNj4UD5Ok7YkYbcbg&oe=65A9BA46",
                  "resized_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418523178_768334495313454_2919812437921070975_n.jpg?stp=dst-jpg_s600x600&_nc_cat=102&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=cJUWBz0HgxAAX-s8hBj&_nc_ht=scontent-atl3-2.xx&oh=00_AfBlG9eRCf0zb7TtquERomVivpWdX_2fMu8WSuuFUvix7Q&oe=65A86FDC",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwfm-staf-caro-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-frm2srs-static-11ar-ban-educm-na-na-na-na-na-fbcar4-04063130"
                }
              ],
              "body_translations": {},
              "byline": None,
              "caption": "education.apple.com",
              "cta_text": "Learn more",
              "dynamic_item_flags": {},
              "dynamic_versions": None,
              "edited_snapshots": [],
              "effective_authorization_category": "NONE",
              "event": [],
              "extra_images": [],
              "extra_links": [],
              "extra_texts": [],
              "extra_videos": [],
              "instagram_shopping_products": [],
              "display_format": "carousel",
              "title": "Apple",
              "link_description": None,
              "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwfm-staf-caro-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-frm2srs-static-11ar-ban-educm-na-na-na-na-na-fbcar1-04063212",
              "page_welcome_message": None,
              "images": [],
              "videos": [],
              "creation_time": 1704850719,
              "page_id": 434174436675167,
              "page_name": "Apple",
              "page_profile_picture_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/416381376_1926936241034123_3049796593831001264_n.jpg?stp=dst-jpg_s60x60&_nc_cat=103&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=6YlerfKrxqgAX98Qy29&_nc_ht=scontent-atl3-1.xx&oh=00_AfDwpO4mhTTAR103ztAEC4I5NJYOCoY3ES5wJmWPJYvL5w&oe=65A8280B",
              "page_categories": {
                "2201": "Product/service"
              },
              "page_entity_type": "person_profile",
              "page_is_profile_page": False,
              "instagram_actor_name": "",
              "instagram_profile_pic_url": "",
              "instagram_url": "",
              "instagram_handle": "",
              "is_reshared": False,
              "version": 3,
              "body": {
                "context": {},
                "markup": {
                  "__html": "Help improve literacy skills for all learners with creative lesson ideas on iPad, and find free teaching resources in the Apple Education Community."
                },
                "callerHash": "f56557a758f1ef4e5affe711ab135709"
              },
              "brazil_tax_id": None,
              "branded_content": None,
              "current_page_name": "Apple",
              "disclaimer_label": None,
              "page_like_count": 13814619,
              "page_profile_uri": "https://facebook.com/apple",
              "page_is_deleted": False,
              "root_reshared_post": None,
              "cta_type": "LEARN_MORE",
              "additional_info": None,
              "ec_certificates": None,
              "country_iso_code": None,
              "instagram_branded_content": None
            },
            "spend": None,
            "startDate": 1704787200,
            "stateMediaRunLabel": None,
            "publisherPlatform": [
              "facebook"
            ],
            "menuItems": []
          }
        ],
        [
          {
            "adid": "0",
            "adArchiveID": "404622588572404",
            "archiveTypes": [],
            "categories": [
              0
            ],
            "containsDigitallyCreatedMedia": False,
            "containsSensitiveContent": False,
            "collationCount": 4,
            "collationID": 3618319331742782,
            "currency": "",
            "endDate": 1705132800,
            "entityType": "person_profile",
            "fevInfo": None,
            "gatedType": "eligible",
            "hasUserReported": False,
            "hiddenSafetyData": False,
            "hideDataStatus": "NONE",
            "impressionsWithIndex": {
              "impressionsText": None,
              "impressionsIndex": -1
            },
            "isAAAEligible": False,
            "isActive": True,
            "isProfilePage": True,
            "pageID": "434174436675167",
            "pageInfo": None,
            "pageIsDeleted": False,
            "pageName": "Apple",
            "politicalCountries": [],
            "reachEstimate": None,
            "reportCount": None,
            "snapshot": {
              "ad_creative_id": "120204523543460150",
              "cards": [
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418418185_313898961009628_6019373429076290890_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=r12pFuvSdLgAX8dH-a0&_nc_ht=scontent-atl3-1.xx&oh=00_AfADrtmJrwGBC6mKnuyq0TolaHtFJIPc6KgzcQvKtHbaNw&oe=65A826E2",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418421878_283044164782661_1102604874158918593_n.jpg?stp=dst-jpg_s600x600&_nc_cat=103&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=amDfcxoV7hIAX8sVBfr&_nc_ht=scontent-atl3-1.xx&oh=00_AfBxxxyuRtz9oL3FIinNl8w_0ko82okVwpg86vgOfrArjg&oe=65A9EE4F",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwim-staf-caro-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-frm2asrs-static-11ar-ban-educm-na-na-na-na-na-igcar1-04063210"
                },
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418726769_660327849385519_6145095768370342582_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=_DU2wq0W_HoAX955ZQ-&_nc_ht=scontent-atl3-1.xx&oh=00_AfDAgK_g2BqCKkuLSfR6C4Ikl373zn68o6c8xM33KaGV0w&oe=65A8C743",
                  "resized_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418728917_1489629534947400_2529946609996892743_n.jpg?stp=dst-jpg_s600x600&_nc_cat=102&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=Ypb3BfK3wnwAX_5FKbI&_nc_ht=scontent-atl3-2.xx&oh=00_AfAu3VocPzLhMZTz8jmR_je48Trf0X_AglX4-tGhR5wq1Q&oe=65A85118",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwim-staf-caro-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-frm2asrs-static-11ar-ban-educm-na-na-na-na-na-igcar2-04063122"
                },
                {
                  "original_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418870308_7047664758648165_4106139340121688896_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=1MeA_iYwQQ8AX__cCi2&_nc_ht=scontent-atl3-2.xx&oh=00_AfC7t_QBKe0Ipj33DYr_iFcV_3YjbyjH3CszeDr6e-kybw&oe=65A8BD2D",
                  "resized_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418729389_1047301569896459_448110494190043623_n.jpg?stp=dst-jpg_s600x600&_nc_cat=102&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=PS2V1CIVkd4AX_2TJvn&_nc_ht=scontent-atl3-2.xx&oh=00_AfC4c9DkWpZFS73eUe6VgNz96Lyqf_i2g2wqfNU0mFKU2Q&oe=65A9D83C",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwim-staf-caro-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-frm2asrs-static-11ar-ban-educm-na-na-na-na-na-igcar3-04063123"
                },
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418730800_280929921660921_1843372706027041816_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=SVYhHqDYGVMAX9gkqIw&_nc_ht=scontent-atl3-1.xx&oh=00_AfDsTUoXIJTI57V6clHCib-WEy1c4e3WKHNdXj419L7-bQ&oe=65A9F0FA",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418953454_926971785516430_1647918054467457355_n.jpg?stp=dst-jpg_s600x600&_nc_cat=107&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=s8Jv0YWRJPIAX8-ykfa&_nc_ht=scontent-atl3-1.xx&oh=00_AfCwqYRjF1XlNRfMCjYYWb5MibcS1KJ-lpSWJ_kw8sC-aQ&oe=65A933B0",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwim-staf-caro-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-frm2asrs-static-11ar-ban-educm-na-na-na-na-na-igcar4-04063124"
                }
              ],
              "body_translations": {},
              "byline": None,
              "caption": "education.apple.com",
              "cta_text": "Learn more",
              "dynamic_item_flags": {},
              "dynamic_versions": None,
              "edited_snapshots": [],
              "effective_authorization_category": "NONE",
              "event": [],
              "extra_images": [],
              "extra_links": [],
              "extra_texts": [],
              "extra_videos": [],
              "instagram_shopping_products": [],
              "display_format": "carousel",
              "title": None,
              "link_description": None,
              "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwim-staf-caro-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-frm2asrs-static-11ar-ban-educm-na-na-na-na-na-igcar1-04063210",
              "page_welcome_message": None,
              "images": [],
              "videos": [],
              "creation_time": 1704850722,
              "page_id": 434174436675167,
              "page_name": "Apple",
              "page_profile_picture_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418730201_720427803388812_8733508269189718279_n.jpg?stp=dst-jpg_s60x60&_nc_cat=101&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=lGXgf5sDXH8AX9s0lZY&_nc_ht=scontent-atl3-2.xx&oh=00_AfA4azdsU0hUUFg8jJAVUPQSw9Zpv2seZqnyLcbkHwD-XQ&oe=65A989F6",
              "page_categories": {
                "2201": "Product/service"
              },
              "page_entity_type": "person_profile",
              "page_is_profile_page": False,
              "instagram_actor_name": "apple",
              "instagram_profile_pic_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418730551_3782616692026042_4692107422082074697_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=gPfTl9WEIIcAX9ONL_a&_nc_ht=scontent-atl3-1.xx&oh=00_AfBCHSzyolZ1O3RHW5NgvOUfwPu-qAYk0d4WHeb16oJzyQ&oe=65AA1193",
              "instagram_url": "",
              "instagram_handle": "",
              "is_reshared": False,
              "version": 3,
              "body": {
                "context": {},
                "markup": {
                  "__html": "Help improve literacy skills for all learners with creative lesson ideas on iPad, and find free teaching resources in the Apple Education Community."
                },
                "callerHash": "f56557a758f1ef4e5affe711ab135709"
              },
              "brazil_tax_id": None,
              "branded_content": None,
              "current_page_name": "Apple",
              "disclaimer_label": None,
              "page_like_count": 13814619,
              "page_profile_uri": "https://facebook.com/apple",
              "page_is_deleted": False,
              "root_reshared_post": None,
              "cta_type": "LEARN_MORE",
              "additional_info": None,
              "ec_certificates": None,
              "country_iso_code": None,
              "instagram_branded_content": None
            },
            "spend": None,
            "startDate": 1704787200,
            "stateMediaRunLabel": None,
            "publisherPlatform": [
              "instagram"
            ],
            "menuItems": []
          },
          {
            "adid": "0",
            "adArchiveID": "285913444103615",
            "archiveTypes": [],
            "categories": [
              0
            ],
            "containsDigitallyCreatedMedia": False,
            "containsSensitiveContent": False,
            "collationCount": None,
            "collationID": 3618319331742782,
            "currency": "",
            "endDate": 1705132800,
            "entityType": "person_profile",
            "fevInfo": None,
            "gatedType": "eligible",
            "hasUserReported": False,
            "hiddenSafetyData": False,
            "hideDataStatus": "NONE",
            "impressionsWithIndex": {
              "impressionsText": None,
              "impressionsIndex": -1
            },
            "isAAAEligible": False,
            "isActive": True,
            "isProfilePage": True,
            "pageID": "434174436675167",
            "pageInfo": None,
            "pageIsDeleted": False,
            "pageName": "Apple",
            "politicalCountries": [],
            "reachEstimate": None,
            "reportCount": None,
            "snapshot": {
              "ad_creative_id": "120204523543320150",
              "cards": [
                {
                  "original_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418584080_1171674770479134_2510117494763802383_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=cmEvYfT5DHAAX-ugr63&_nc_ht=scontent-atl3-2.xx&oh=00_AfAMNoCGfxrlFyWU-wdoVjztl5EKz7jfpskJ7CkO9uh-cw&oe=65A8960C",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418545350_1533722364096633_7220230876389627971_n.jpg?stp=dst-jpg_s600x600&_nc_cat=108&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=OBysiJBDrcAAX_iULSf&_nc_ht=scontent-atl3-1.xx&oh=00_AfBxPlC__fDPHNeyV7tHpicqvubQ251qx1ouBYKInjQRtw&oe=65A87599",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwfm-staf-caro-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-frm2asrs-static-11ar-ban-educm-na-na-na-na-na-fbcar1-04063213"
                },
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418563638_354951383987287_6996000288217237502_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=KqO6GUyt0X4AX9xx5KZ&_nc_ht=scontent-atl3-1.xx&oh=00_AfBmPR2f9fF0czeBd2_3Y3OPGROhvXKz5SG9aJoPCutDvg&oe=65A8A534",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418554100_1434844830401525_1904425384229185862_n.jpg?stp=dst-jpg_s600x600&_nc_cat=107&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=dhMS3LXiN5oAX9_LtmI&_nc_ht=scontent-atl3-1.xx&oh=00_AfAsmbWNJ-8t3Ec1E-i0IfqBMTgIVa09oKg1R1hV5sVRFw&oe=65AA11FD",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwfm-staf-caro-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-frm2asrs-static-11ar-ban-educm-na-na-na-na-na-fbcar2-04063131"
                },
                {
                  "original_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418568925_905056861323924_5301762740068803228_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=UjMxsD3PYPAAX_AOsU6&_nc_ht=scontent-atl3-2.xx&oh=00_AfA2NRzjUlsLpntFlgloEqjnesEqELhpWIoKmkmDsohh-g&oe=65A9942C",
                  "resized_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418545577_378014274880527_9187291034003901054_n.jpg?stp=dst-jpg_s600x600&_nc_cat=101&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=1MFy99BVu1sAX95_n1X&_nc_ht=scontent-atl3-2.xx&oh=00_AfBtKkR30c7IQxCYmFTINCfycuZFrVI6cV7ngbnQFxf01A&oe=65A9395F",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwfm-staf-caro-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-frm2asrs-static-11ar-ban-educm-na-na-na-na-na-fbcar3-04063132"
                },
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418568772_369041915818093_7286937552091809553_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=PURjLAz7WckAX8dWW0Y&_nc_ht=scontent-atl3-1.xx&oh=00_AfCFp_fIQQmYmAHAvsFfdm_EyO0nZPcuOOQulBorYZSxSQ&oe=65A8F5F5",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418542806_207777152418432_1510153823064336312_n.jpg?stp=dst-jpg_s600x600&_nc_cat=108&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=GRnI2oewR2kAX-Vanln&_nc_ht=scontent-atl3-1.xx&oh=00_AfCuaellZ76f2M8G3kjO6ugpwmISBpujkL9vqs5SMSk7kA&oe=65A90EF6",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwfm-staf-caro-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-frm2asrs-static-11ar-ban-educm-na-na-na-na-na-fbcar4-04063133"
                }
              ],
              "body_translations": {},
              "byline": None,
              "caption": "education.apple.com",
              "cta_text": "Learn more",
              "dynamic_item_flags": {},
              "dynamic_versions": None,
              "edited_snapshots": [],
              "effective_authorization_category": "NONE",
              "event": [],
              "extra_images": [],
              "extra_links": [],
              "extra_texts": [],
              "extra_videos": [],
              "instagram_shopping_products": [],
              "display_format": "carousel",
              "title": "Apple",
              "link_description": None,
              "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwfm-staf-caro-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-frm2asrs-static-11ar-ban-educm-na-na-na-na-na-fbcar1-04063213",
              "page_welcome_message": None,
              "images": [],
              "videos": [],
              "creation_time": 1704850721,
              "page_id": 434174436675167,
              "page_name": "Apple",
              "page_profile_picture_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418554959_378829604552989_7675133279260953576_n.jpg?stp=dst-jpg_s60x60&_nc_cat=110&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=DeTYV7E5mTwAX_guZz3&_nc_ht=scontent-atl3-1.xx&oh=00_AfAaYQW1hAFYd7_3ClVfYwr7rtIHhtk0z86wcrMsD8O8OQ&oe=65A9926E",
              "page_categories": {
                "2201": "Product/service"
              },
              "page_entity_type": "person_profile",
              "page_is_profile_page": False,
              "instagram_actor_name": "",
              "instagram_profile_pic_url": "",
              "instagram_url": "",
              "instagram_handle": "",
              "is_reshared": False,
              "version": 3,
              "body": {
                "context": {},
                "markup": {
                  "__html": "Help improve literacy skills for all learners with creative lesson ideas on iPad, and find free teaching resources in the Apple Education Community."
                },
                "callerHash": "f56557a758f1ef4e5affe711ab135709"
              },
              "brazil_tax_id": None,
              "branded_content": None,
              "current_page_name": "Apple",
              "disclaimer_label": None,
              "page_like_count": 13814619,
              "page_profile_uri": "https://facebook.com/apple",
              "page_is_deleted": False,
              "root_reshared_post": None,
              "cta_type": "LEARN_MORE",
              "additional_info": None,
              "ec_certificates": None,
              "country_iso_code": None,
              "instagram_branded_content": None
            },
            "spend": None,
            "startDate": 1704787200,
            "stateMediaRunLabel": None,
            "publisherPlatform": [
              "facebook"
            ],
            "menuItems": []
          },
          {
            "adid": "0",
            "adArchiveID": "1034640374460772",
            "archiveTypes": [],
            "categories": [
              0
            ],
            "containsDigitallyCreatedMedia": False,
            "containsSensitiveContent": False,
            "collationCount": None,
            "collationID": 3618319331742782,
            "currency": "",
            "endDate": 1705132800,
            "entityType": "person_profile",
            "fevInfo": None,
            "gatedType": "eligible",
            "hasUserReported": False,
            "hiddenSafetyData": False,
            "hideDataStatus": "NONE",
            "impressionsWithIndex": {
              "impressionsText": None,
              "impressionsIndex": -1
            },
            "isAAAEligible": False,
            "isActive": True,
            "isProfilePage": True,
            "pageID": "434174436675167",
            "pageInfo": None,
            "pageIsDeleted": False,
            "pageName": "Apple",
            "politicalCountries": [],
            "reachEstimate": None,
            "reportCount": None,
            "snapshot": {
              "ad_creative_id": "120204523543230150",
              "cards": [
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418571634_399637072538124_4393180933521375007_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=fAs9dg2Dzc4AX_wXKHB&_nc_ht=scontent-atl3-1.xx&oh=00_AfCRFSIgfZ32a85BMIbTV3LBF2H12hLfYXdVDteLm1aIKg&oe=65A92D13",
                  "resized_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418523880_2104669976540303_4630132199218663082_n.jpg?stp=dst-jpg_s600x600&_nc_cat=102&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=ZrfyZNqKqIoAX__VQjL&_nc_ht=scontent-atl3-2.xx&oh=00_AfCx_rEyqbb7pwMkChoGobJkYtgPp4r79uZoVITCd-tIRA&oe=65A8A1DA",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwfm-staf-caro-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-frm2asrs-static-11ar-ban-educm-na-na-na-na-na-fbcar1-04063207"
                },
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/416368476_864586575361329_882219686910733474_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=poRU0C9cA4gAX9CZpi5&_nc_ht=scontent-atl3-1.xx&oh=00_AfA2LHD_O6RzS9sfCpK3LBS_N_y6_KDlmLJX-255-gC7Uw&oe=65A9285B",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418504266_1292994498042593_3693681160586817633_n.jpg?stp=dst-jpg_s600x600&_nc_cat=100&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=BEJLmI9wFAAAX-p8RA1&_nc_ht=scontent-atl3-1.xx&oh=00_AfCYFn-z3ZPfLAdyXozb9UusushkY9NRvfyI5sw926HpAQ&oe=65A8D9AB",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwfm-staf-caro-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-frm2asrs-static-11ar-ban-educm-na-na-na-na-na-fbcar2-04063113"
                },
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/416472330_868140175094411_2534400081619096960_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=nM8MpEJbBRkAX_3jgst&_nc_ht=scontent-atl3-1.xx&oh=00_AfAsacadgUBfT18p5MCUSaC-IfZpOMywHKsnYzsvXmzbSw&oe=65A8A735",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418538143_3401745316804126_7250600238405365248_n.jpg?stp=dst-jpg_s600x600&_nc_cat=100&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=UyJU3_EXa8gAX9Jtl6a&_nc_ht=scontent-atl3-1.xx&oh=00_AfB_BaNUiLmrPatvCyTe34wtGl_gpLmBUWthec8_2F1ArA&oe=65A88CEA",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwfm-staf-caro-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-frm2asrs-static-11ar-ban-educm-na-na-na-na-na-fbcar3-04063114"
                },
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/416355426_914363893377667_6931122391287008564_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=GHPb05VGOXsAX-DV-W7&_nc_ht=scontent-atl3-1.xx&oh=00_AfCK5yBusbvnwCmx41X0ZQEai16Nx9F9sjyKJw72P8LadQ&oe=65A92FA8",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/416329821_298006269427671_1395099788156468393_n.jpg?stp=dst-jpg_s600x600&_nc_cat=108&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=qFZ3GfOWgYYAX-Ni3LK&_nc_ht=scontent-atl3-1.xx&oh=00_AfD7lkwWCpYHqak4OMoerQWLktHXgTuJnA5RrB2SK_fEKg&oe=65A90FD3",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwfm-staf-caro-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-frm2asrs-static-11ar-ban-educm-na-na-na-na-na-fbcar4-04063115"
                }
              ],
              "body_translations": {},
              "byline": None,
              "caption": "education.apple.com",
              "cta_text": "Learn more",
              "dynamic_item_flags": {},
              "dynamic_versions": None,
              "edited_snapshots": [],
              "effective_authorization_category": "NONE",
              "event": [],
              "extra_images": [],
              "extra_links": [],
              "extra_texts": [],
              "extra_videos": [],
              "instagram_shopping_products": [],
              "display_format": "carousel",
              "title": "Apple",
              "link_description": None,
              "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwfm-staf-caro-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-frm2asrs-static-11ar-ban-educm-na-na-na-na-na-fbcar1-04063207",
              "page_welcome_message": None,
              "images": [],
              "videos": [],
              "creation_time": 1704850721,
              "page_id": 434174436675167,
              "page_name": "Apple",
              "page_profile_picture_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418524299_1724331141414398_7293885890683712761_n.jpg?stp=dst-jpg_s60x60&_nc_cat=105&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=GFCGYnNBEs4AX8hJkYz&_nc_ht=scontent-atl3-2.xx&oh=00_AfAi2KD_i1TtiNN_GXMpIuFrbujtz61pTPR5nG8PwcIDYA&oe=65AA1A05",
              "page_categories": {
                "2201": "Product/service"
              },
              "page_entity_type": "person_profile",
              "page_is_profile_page": False,
              "instagram_actor_name": "",
              "instagram_profile_pic_url": "",
              "instagram_url": "",
              "instagram_handle": "",
              "is_reshared": False,
              "version": 3,
              "body": {
                "context": {},
                "markup": {
                  "__html": "Help improve literacy skills for all learners with creative lesson ideas on iPad, and find free teaching resources in the Apple Education Community."
                },
                "callerHash": "f56557a758f1ef4e5affe711ab135709"
              },
              "brazil_tax_id": None,
              "branded_content": None,
              "current_page_name": "Apple",
              "disclaimer_label": None,
              "page_like_count": 13814619,
              "page_profile_uri": "https://facebook.com/apple",
              "page_is_deleted": False,
              "root_reshared_post": None,
              "cta_type": "LEARN_MORE",
              "additional_info": None,
              "ec_certificates": None,
              "country_iso_code": None,
              "instagram_branded_content": None
            },
            "spend": None,
            "startDate": 1704787200,
            "stateMediaRunLabel": None,
            "publisherPlatform": [
              "facebook"
            ],
            "menuItems": []
          }
        ],
        [
          {
            "adid": "0",
            "adArchiveID": "749064870587587",
            "archiveTypes": [],
            "categories": [
              0
            ],
            "containsDigitallyCreatedMedia": False,
            "containsSensitiveContent": False,
            "collationCount": 1,
            "collationID": 1762912090877850,
            "currency": "",
            "endDate": 1705132800,
            "entityType": "person_profile",
            "fevInfo": None,
            "gatedType": "eligible",
            "hasUserReported": False,
            "hiddenSafetyData": False,
            "hideDataStatus": "NONE",
            "impressionsWithIndex": {
              "impressionsText": None,
              "impressionsIndex": -1
            },
            "isAAAEligible": False,
            "isActive": True,
            "isProfilePage": True,
            "pageID": "434174436675167",
            "pageInfo": None,
            "pageIsDeleted": False,
            "pageName": "Apple",
            "politicalCountries": [],
            "reachEstimate": None,
            "reportCount": None,
            "snapshot": {
              "ad_creative_id": "120204523543000150",
              "cards": [
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/416373428_245116608617083_5712108675729977180_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=xC0sQgLLVIUAX-0wtgJ&_nc_ht=scontent-atl3-1.xx&oh=00_AfCQyap7VOK93fxBkg_AvFXVpsl3viNgisQjzkMD6EGvbw&oe=65A8E529",
                  "resized_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418586406_315730794145275_4625558784639958185_n.jpg?stp=dst-jpg_s600x600&_nc_cat=108&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=iyliG8NC3BIAX9rERJl&_nc_ht=scontent-atl3-1.xx&oh=00_AfBTjlKg2zYrSMXvWOB5heD0R2hcOVbcAQX12nrZQbArTA&oe=65A9B3F7",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwim-staf-caro-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-frm2asrs-static-11ar-ban-educm-na-na-na-na-na-igcar1-04063216"
                },
                {
                  "original_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418534725_378003688214128_2711966963052650955_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=q2HlSPTMA4YAX9sEd2N&_nc_ht=scontent-atl3-2.xx&oh=00_AfBF9IDm3URx41VmGsUgVjcJlAr_k7w1Kxxemi6jmtZnHQ&oe=65A83F83",
                  "resized_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418544714_743519323967020_8583999459831946688_n.jpg?stp=dst-jpg_s600x600&_nc_cat=105&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=ektaRKzoiR8AX-J13Vp&_nc_ht=scontent-atl3-2.xx&oh=00_AfBhn6msaME-HdQoRfaNCpAz9cIAKzN4Z5Gzkm1QicRLVQ&oe=65A87D4C",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwim-staf-caro-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-frm2asrs-static-11ar-ban-educm-na-na-na-na-na-igcar2-04063140"
                },
                {
                  "original_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/416388131_775576761058253_727015936372497848_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=VyjfgQ-c5cEAX9bJyl6&_nc_ht=scontent-atl3-1.xx&oh=00_AfCuDVSxNXmmR0dyeP0G5HEgm3pzfERAN4o6w0psrGIXqg&oe=65A8D519",
                  "resized_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/416341185_1820360788400256_5723436040242311061_n.jpg?stp=dst-jpg_s600x600&_nc_cat=111&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=KORIaruwqE0AX-D5xw3&_nc_ht=scontent-atl3-2.xx&oh=00_AfDeL8qIZQ5D8SIqoHSiWbDTZbjb5lN_-neacQcdwrxwZA&oe=65A95F51",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwim-staf-caro-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-frm2asrs-static-11ar-ban-educm-na-na-na-na-na-igcar3-04063141"
                },
                {
                  "original_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/416330110_308301571632185_5712990492487692981_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=e5gJsCmt4qoAX-yLf-C&_nc_ht=scontent-atl3-2.xx&oh=00_AfAVit5eYKi0Hzz3O0fucouXD7ARJK62SMelQ1gVgwfmGw&oe=65A96DF3",
                  "resized_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418509941_281426664591796_3517577972811475060_n.jpg?stp=dst-jpg_s600x600&_nc_cat=101&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=V8lGlpQf4W0AX8V_aiN&_nc_ht=scontent-atl3-2.xx&oh=00_AfCT-914EWYQoWQiyP6TR_N9OuM4hNvc20KItjzm5S9pgw&oe=65A932F2",
                  "watermarked_resized_image_url": "",
                  "image_crops": {},
                  "body": " ",
                  "caption": "education.apple.com",
                  "cta_type": "LEARN_MORE",
                  "cta_text": "Learn More",
                  "title": " ",
                  "link_description": " ",
                  "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwim-staf-caro-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-frm2asrs-static-11ar-ban-educm-na-na-na-na-na-igcar4-04063142"
                }
              ],
              "body_translations": {},
              "byline": None,
              "caption": "education.apple.com",
              "cta_text": "Learn more",
              "dynamic_item_flags": {},
              "dynamic_versions": None,
              "edited_snapshots": [],
              "effective_authorization_category": "NONE",
              "event": [],
              "extra_images": [],
              "extra_links": [],
              "extra_texts": [],
              "extra_videos": [],
              "instagram_shopping_products": [],
              "display_format": "carousel",
              "title": None,
              "link_description": None,
              "link_url": "https://education.apple.com/forum/teaching-and-learning?cid=eduent-us-soc-apedu-nyni-socl-rbwim-staf-caro-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-frm2asrs-static-11ar-ban-educm-na-na-na-na-na-igcar1-04063216",
              "page_welcome_message": None,
              "images": [],
              "videos": [],
              "creation_time": 1704850719,
              "page_id": 434174436675167,
              "page_name": "Apple",
              "page_profile_picture_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418532481_266592156210504_5312817547257516338_n.jpg?stp=dst-jpg_s60x60&_nc_cat=102&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=TI0nhoosXXkAX-Ulm2S&_nc_ht=scontent-atl3-2.xx&oh=00_AfCVkAL-iPxgEI4Zoj2QTJw5SxsZg4Wi9fpcnVZH6FCcCQ&oe=65A96C17",
              "page_categories": {
                "2201": "Product/service"
              },
              "page_entity_type": "person_profile",
              "page_is_profile_page": False,
              "instagram_actor_name": "apple",
              "instagram_profile_pic_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418550905_3233247400308751_1414035569483070953_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=7xFJ89_GIkoAX8o-BLU&_nc_ht=scontent-atl3-1.xx&oh=00_AfB3ecj226b2AvxhWxCB2YEiK9SSopCx_ad3_eYOeZH_8w&oe=65A93A9F",
              "instagram_url": "",
              "instagram_handle": "",
              "is_reshared": False,
              "version": 3,
              "body": {
                "context": {},
                "markup": {
                  "__html": "Help improve literacy skills for all learners with creative lesson ideas on iPad, and find free teaching resources in the Apple Education Community."
                },
                "callerHash": "f56557a758f1ef4e5affe711ab135709"
              },
              "brazil_tax_id": None,
              "branded_content": None,
              "current_page_name": "Apple",
              "disclaimer_label": None,
              "page_like_count": 13814619,
              "page_profile_uri": "https://facebook.com/apple",
              "page_is_deleted": False,
              "root_reshared_post": None,
              "cta_type": "LEARN_MORE",
              "additional_info": None,
              "ec_certificates": None,
              "country_iso_code": None,
              "instagram_branded_content": None
            },
            "spend": None,
            "startDate": 1704787200,
            "stateMediaRunLabel": None,
            "publisherPlatform": [
              "instagram"
            ],
            "menuItems": []
          }
        ],
        [
          {
            "adid": "0",
            "adArchiveID": "1077055086776144",
            "archiveTypes": [],
            "categories": [
              0
            ],
            "containsDigitallyCreatedMedia": False,
            "containsSensitiveContent": False,
            "collationCount": 4,
            "collationID": 290728066915679,
            "currency": "",
            "endDate": 1705132800,
            "entityType": "person_profile",
            "fevInfo": None,
            "gatedType": "eligible",
            "hasUserReported": False,
            "hiddenSafetyData": False,
            "hideDataStatus": "NONE",
            "impressionsWithIndex": {
              "impressionsText": None,
              "impressionsIndex": -1
            },
            "isAAAEligible": False,
            "isActive": True,
            "isProfilePage": True,
            "pageID": "434174436675167",
            "pageInfo": None,
            "pageIsDeleted": False,
            "pageName": "Apple",
            "politicalCountries": [],
            "reachEstimate": None,
            "reportCount": None,
            "snapshot": {
              "ad_creative_id": "120204523260490150",
              "cards": [],
              "body_translations": {},
              "byline": None,
              "caption": "education.apple.com",
              "cta_text": "Learn more",
              "dynamic_item_flags": {},
              "dynamic_versions": None,
              "edited_snapshots": [],
              "effective_authorization_category": "NONE",
              "event": [],
              "extra_images": [],
              "extra_links": [],
              "extra_texts": [],
              "extra_videos": [],
              "instagram_shopping_products": [],
              "display_format": "video",
              "title": None,
              "link_description": None,
              "link_url": "https://education.apple.com/resource/250010000?cid=eduent-us-soc-apedu-nyni-socl-rbwim-intd-infe-cpc-ios-mul-aiost-bhv-tchr-edulp-ufnnl-usen-apllv-andis-11ar-13s-educm-na-na-na-na-na-na-04063032",
              "page_welcome_message": None,
              "images": [],
              "videos": [
                {
                  "video_hd_url": "https://video-atl3-1.xx.fbcdn.net/v/t42.1790-2/417476586_1077055106776142_7422294183109901166_n.?_nc_cat=103&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=5K8Lx1nlecAAX8ycPPp&_nc_ht=video-atl3-1.xx&oh=00_AfDnbyeWkxH2-8ASgm9fUni5GsajqJvugXopBETCb3lIJw&oe=65A85CB6",
                  "video_sd_url": "https://video-atl3-2.xx.fbcdn.net/v/t42.1790-2/416507837_286601494414340_3144469426579331189_n.mp4?_nc_cat=104&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=MtozmKlcBnsAX_840Xt&_nc_ht=video-atl3-2.xx&oh=00_AfARO4NMAXrid4-CZcQVXYhqDLp55gPc0pMQBBtAogRoxQ&oe=65A9A574",
                  "watermarked_video_sd_url": "",
                  "watermarked_video_hd_url": "",
                  "video_preview_image_url": "https://scontent-atl3-2.xx.fbcdn.net/v/t39.35426-6/418527661_752895356684265_8022994671332313302_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=b2mzX8cw3DgAX-WX8c1&_nc_ht=scontent-atl3-2.xx&oh=00_AfCVsp0ssL8CYfUdH_c09bMECQMIC11gg_NZvTc4ll3tPg&oe=65A9AFD2"
                }
              ],
              "creation_time": 1704849395,
              "page_id": 434174436675167,
              "page_name": "Apple",
              "page_profile_picture_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/416385046_1350813085611854_7756926685027742353_n.jpg?stp=dst-jpg_s60x60&_nc_cat=107&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=2FCDhLhW3isAX_V7PY7&_nc_ht=scontent-atl3-1.xx&oh=00_AfDMytuZJIMtZ6_AIkWLzrNpSBlefRqYLmHNSPPjkxEybQ&oe=65A9DFC5",
              "page_categories": {
                "2201": "Product/service"
              },
              "page_entity_type": "person_profile",
              "page_is_profile_page": False,
              "instagram_actor_name": "apple",
              "instagram_profile_pic_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418520018_1127539795259690_8853598521549748193_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=x45q8zFMikcAX_z_Gyw&_nc_ht=scontent-atl3-1.xx&oh=00_AfD6IRzD7oQxgRPQDo1hdtMMo7XFTlpLRQhzvU8AnbeZyQ&oe=65A9F387",
              "instagram_url": "",
              "instagram_handle": "",
              "is_reshared": False,
              "version": 3,
              "body": {
                "context": {},
                "markup": {
                  "__html": "Kick off the new year with hands-on learning for educators using iPad and Mac.<br /> <br /> Explore helpful resources and practice new skills in these free virtual sessions."
                },
                "callerHash": "f56557a758f1ef4e5affe711ab135709"
              },
              "brazil_tax_id": None,
              "branded_content": None,
              "current_page_name": "Apple",
              "disclaimer_label": None,
              "page_like_count": 13814619,
              "page_profile_uri": "https://facebook.com/apple",
              "page_is_deleted": False,
              "root_reshared_post": None,
              "cta_type": "LEARN_MORE",
              "additional_info": None,
              "ec_certificates": None,
              "country_iso_code": None,
              "instagram_branded_content": None
            },
            "spend": None,
            "startDate": 1704787200,
            "stateMediaRunLabel": None,
            "publisherPlatform": [
              "instagram"
            ],
            "menuItems": []
          },
          {
            "adid": "0",
            "adArchiveID": "3633375103570384",
            "archiveTypes": [],
            "categories": [
              0
            ],
            "containsDigitallyCreatedMedia": False,
            "containsSensitiveContent": False,
            "collationCount": None,
            "collationID": 290728066915679,
            "currency": "",
            "endDate": 1705132800,
            "entityType": "person_profile",
            "fevInfo": None,
            "gatedType": "eligible",
            "hasUserReported": False,
            "hiddenSafetyData": False,
            "hideDataStatus": "NONE",
            "impressionsWithIndex": {
              "impressionsText": None,
              "impressionsIndex": -1
            },
            "isAAAEligible": False,
            "isActive": True,
            "isProfilePage": True,
            "pageID": "434174436675167",
            "pageInfo": None,
            "pageIsDeleted": False,
            "pageName": "Apple",
            "politicalCountries": [],
            "reachEstimate": None,
            "reportCount": None,
            "snapshot": {
              "ad_creative_id": "120204523260530150",
              "cards": [],
              "body_translations": {},
              "byline": None,
              "caption": "education.apple.com",
              "cta_text": "Learn more",
              "dynamic_item_flags": {},
              "dynamic_versions": None,
              "edited_snapshots": [],
              "effective_authorization_category": "NONE",
              "event": [],
              "extra_images": [],
              "extra_links": [],
              "extra_texts": [],
              "extra_videos": [],
              "instagram_shopping_products": [],
              "display_format": "video",
              "title": None,
              "link_description": None,
              "link_url": "https://education.apple.com/resource/250010000?cid=eduent-us-soc-apedu-nyni-socl-rbwim-intd-infe-cpc-and-mul-aandt-bhv-tchr-edulp-ufnnl-usen-apllv-andis-11ar-13s-educm-na-na-na-na-na-na-04063048",
              "page_welcome_message": None,
              "images": [],
              "videos": [
                {
                  "video_hd_url": "https://video-atl3-2.xx.fbcdn.net/v/t42.1790-2/418485086_3633375116903716_8189687981136668961_n.?_nc_cat=105&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=eOo_28YSlBIAX-gComU&_nc_ht=video-atl3-2.xx&oh=00_AfDjFPhV6YHxEpvBqyyXDDcJ-Prarw_1wJNLSNN7trDGSA&oe=65AA1723",
                  "video_sd_url": "https://video-atl3-2.xx.fbcdn.net/v/t42.1790-2/416507837_286601494414340_3144469426579331189_n.mp4?_nc_cat=104&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=MtozmKlcBnsAX_840Xt&_nc_ht=video-atl3-2.xx&oh=00_AfARO4NMAXrid4-CZcQVXYhqDLp55gPc0pMQBBtAogRoxQ&oe=65A9A574",
                  "watermarked_video_sd_url": "",
                  "watermarked_video_hd_url": "",
                  "video_preview_image_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/416370339_259332577176802_1015497872913894579_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=2EEdufxavy8AX8TrGij&_nc_ht=scontent-atl3-1.xx&oh=00_AfBNTHdSzzDc53fjWHKJI1IiC1wmpdT5ypASwi2vggaodQ&oe=65A8FF74"
                }
              ],
              "creation_time": 1704849376,
              "page_id": 434174436675167,
              "page_name": "Apple",
              "page_profile_picture_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/418554863_752151223450735_3615988790809359788_n.jpg?stp=dst-jpg_s60x60&_nc_cat=106&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=uqGS1-7dAQkAX93en6X&_nc_oc=AQnCzCC0Q2nxD1yfcIXcn_EdGlAi3QaWjRgCaZKTMA8frMokTZ3XmYjKgolHRBExnDQ&_nc_ht=scontent-atl3-1.xx&oh=00_AfAeHMG4hDcszHbsqWRFVYaG7rZz2ABCC5mZ-MVwR3mcNw&oe=65A8A8F3",
              "page_categories": {
                "2201": "Product/service"
              },
              "page_entity_type": "person_profile",
              "page_is_profile_page": False,
              "instagram_actor_name": "apple",
              "instagram_profile_pic_url": "https://scontent-atl3-1.xx.fbcdn.net/v/t39.35426-6/416335484_779557710581742_5178083717919700106_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=c53f8f&_nc_ohc=n0NkpFkROv0AX_y7Irf&_nc_ht=scontent-atl3-1.xx&oh=00_AfBzPXmAyiuhjQbIsmZzgRouJYNEViE_Cu5BBf8r9NDv6Q&oe=65A833E2",
              "instagram_url": "",
              "instagram_handle": "",
              "is_reshared": False,
              "version": 3,
              "body": {
                "context": {},
                "markup": {
                  "__html": "Kick off the new year with hands-on learning for educators using iPad and Mac.<br /> <br /> Explore helpful resources and practice new skills in these free virtual sessions."
                },
                "callerHash": "f56557a758f1ef4e5affe711ab135709"
              },
              "brazil_tax_id": None,
              "branded_content": None,
              "current_page_name": "Apple",
              "disclaimer_label": None,
              "page_like_count": 13814619,
              "page_profile_uri": "https://facebook.com/apple",
              "page_is_deleted": False,
              "root_reshared_post": None,
              "cta_type": "LEARN_MORE",
              "additional_info": None,
              "ec_certificates": None,
              "country_iso_code": None,
              "instagram_branded_content": None
            },
            "spend": None,
            "startDate": 1704787200,
            "stateMediaRunLabel": None,
            "publisherPlatform": [
              "instagram"
            ],
            "menuItems": []
          }
        ]
      ]
    }