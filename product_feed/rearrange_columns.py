import pandas
header = [
    'aw_deep_link',
    'description',
    'product_name',
    'aw_image_url',
    'search_price',
    'merchant_name',
    'display_price',
    'brand_name',
    'colour',
    'rrp_price',
    'category_name',
    'Fashion:size',
    'aw_product_id'
]
df = pandas.read_csv('product_feed.csv', sep=';')
df.to_csv('new_product_feed.csv', columns=header, sep=';')

print(df)
