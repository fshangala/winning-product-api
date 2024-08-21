from ScraperSDK import shopify

shop = shopify.ShopifyProduct("https://theendcult.com/products/gothic-zipper-dress-1")
print(shop.data)
