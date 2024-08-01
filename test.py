from ScraperSDK import shopify

shop = shopify.Shopify("https://mycustom-cars.com")
print(shop.themeData)
print(shop.hostname)
print(shop.title)
print(shop.url)
print(shop.shopify_url)
print(shop.locale)
print(shop.currency)
