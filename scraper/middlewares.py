
def cors_middleware(get_response):
  def middleware(request):
    response = get_response(request)
    response["Access-Control-Allow-Headers"] = "*"
    response["Access-Control-Allow-Origin"] = "*"
    return response
  return middleware