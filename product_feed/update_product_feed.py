import urllib.request
import io
import gzip
import os

response = urllib.request.urlopen('https://productdata.awin.com/datafeed/download/apikey/c43cb2adc7d4b494d4d5ef358ef0050d/language/en/fid/2606/bid/63397/columns/aw_deep_link,description,product_name,aw_image_url,search_price,merchant_name,display_price,brand_name,colour,rrp_price,category_name,aw_product_id,merchant_product_id,merchant_image_url,merchant_category/format/csv/delimiter/%2C/compression/gzip/adultcontent/1/')
compressed_file = io.BytesIO(response.read())
decompressed_file = gzip.GzipFile(fileobj=compressed_file)

with open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'product_feed/product_feed'), 'wb') as outfile:
    outfile.write(decompressed_file.read())
    
    
    