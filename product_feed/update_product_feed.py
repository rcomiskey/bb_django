import urllib.request
import io
import gzip
import os

response = urllib.request.urlopen('https://productdata.awin.com/datafeed/download/apikey/c43cb2adc7d4b494d4d5ef358ef0050d/language/en/fid/17383/bid/64307/columns/aw_deep_link,description,product_name,aw_image_url,search_price,merchant_name,display_price,brand_name,colour,rrp_price,category_name,Fashion%3Asize,aw_product_id,merchant_product_id,merchant_image_url,merchant_category,merchant_id,category_id,currency,store_price,delivery_cost,merchant_deep_link,language,last_updated,data_feed_id,brand_id,product_short_description,specifications,condition,product_model,model_number,dimensions,keywords,promotional_text,product_type,commission_group,merchant_product_category_path,merchant_product_second_category,merchant_product_third_category,saving,savings_percent,base_price,base_price_amount,base_price_text,product_price_old,delivery_restrictions,delivery_weight,warranty,terms_of_contract,delivery_time,in_stock,stock_quantity,valid_from,valid_to,is_for_sale,web_offer,pre_order,stock_status,size_stock_status,size_stock_amount,merchant_thumb_url,large_image,alternate_image,aw_thumb_url,alternate_image_two,alternate_image_three,alternate_image_four,reviews,average_rating,rating,number_available,custom_1,custom_2,custom_3,custom_4,custom_5,custom_6,custom_7,custom_8,custom_9,ean,isbn,upc,mpn,parent_product_id,product_GTIN,basket_link,Fashion%3Asuitable_for,Fashion%3Acategory,Fashion%3Amaterial,Fashion%3Apattern,Fashion%3Aswatch/format/csv/delimiter/%3B/compression/gzip/adultcontent/1/')
compressed_file = io.BytesIO(response.read())
decompressed_file = gzip.GzipFile(fileobj=compressed_file)

with open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'product_feed/product_feed'), 'wb') as outfile:
    outfile.write(decompressed_file.read())
    
    
    