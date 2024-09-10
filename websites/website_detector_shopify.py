import requests

def shopify_detector(url)->dict:
  response = requests.get(url)
  index=response.text.find("Shopify.shop")
  if index >= 0:
    return {"name":"shopify"}
  else:
    None