import requests

def shoplazza_detector(url)->dict:
  response = requests.get(url)
  index=response.text.find("window.SHOPLAZZA")
  if index >= 0:
    return {"name":"shoplazza"}
  else:
    None