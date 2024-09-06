from urllib.parse import urlparse

url="https://norvure.com/products/freshlock%E2%84%A2-mason-jar-vacuum-sealer"
print("/products/" in url)

urlp=urlparse(url=url)

print(urlp.scheme,urlp.hostname,urlp.path)