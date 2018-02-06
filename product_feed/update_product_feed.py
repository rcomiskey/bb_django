import urllib.request
import io
import gzip
import os

response = urllib.request.urlopen('https://productdata.awin.com/datafeed/download/apikey/c43cb2adc7d4b494d4d5ef358ef0050d/language/en/fid/2606/bid/64649/columns/aw_deep_link,product_name,aw_product_id,merchant_product_id,merchant_image_url,description,merchant_category,search_price,merchant_name,merchant_id,category_name,category_id,aw_image_url,currency,store_price,delivery_cost,merchant_deep_link,language,last_updated,display_price,data_feed_id/format/csv/delimiter/%2C/compression/gzip/')
compressed_file = io.BytesIO(response.read())
decompressed_file = gzip.GzipFile(fileobj=compressed_file)

with open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'product_feed/product_feed'), 'wb') as outfile:
    outfile.write(decompressed_file.read())
    
    
    