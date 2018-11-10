import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "best_bargain_project.settings")
django.setup()
from products.models import Product, Category, Brand
import csv
import re
import urllib.request
import io
import gzip
import pandas


# Read in CSV from Awin
response = urllib.request.urlopen('https://productdata.awin.com/datafeed/download/apikey/c43cb2adc7d4b494d4d5ef358ef0050d/language/en/fid/17383/bid/64307/columns/aw_deep_link,description,product_name,aw_image_url,search_price,merchant_name,display_price,brand_name,colour,rrp_price,category_name,Fashion%3Asize,aw_product_id,merchant_product_id,merchant_image_url,merchant_category,merchant_id,category_id,currency,store_price,delivery_cost,merchant_deep_link,language,last_updated,data_feed_id,brand_id,product_short_description,specifications,condition,product_model,model_number,dimensions,keywords,promotional_text,product_type,commission_group,merchant_product_category_path,merchant_product_second_category,merchant_product_third_category,saving,savings_percent,base_price,base_price_amount,base_price_text,product_price_old,delivery_restrictions,delivery_weight,warranty,terms_of_contract,delivery_time,in_stock,stock_quantity,valid_from,valid_to,is_for_sale,web_offer,pre_order,stock_status,size_stock_status,size_stock_amount,merchant_thumb_url,large_image,alternate_image,aw_thumb_url,alternate_image_two,alternate_image_three,alternate_image_four,reviews,average_rating,rating,number_available,custom_1,custom_2,custom_3,custom_4,custom_5,custom_6,custom_7,custom_8,custom_9,ean,isbn,upc,mpn,parent_product_id,product_GTIN,basket_link,Fashion%3Asuitable_for,Fashion%3Acategory,Fashion%3Amaterial,Fashion%3Apattern,Fashion%3Aswatch/format/csv/delimiter/%3B/compression/gzip/adultcontent/1/')
compressed_file = io.BytesIO(response.read())
decompressed_file = gzip.GzipFile(fileobj=compressed_file)

with open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'product_feed/product_feed'), 'wb') as outfile:
    outfile.write(decompressed_file.read())

# Remove quotes
with open('product_feed', 'r') as f, open('product_feed.csv', 'w') as fo:
    linecount = 0
    for line in f:
        linecount += 1
        fo.write(line.replace('"', '').replace("'", ""))
    print("{0} rows in CSV".format(linecount))

# Rearrange columns
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

# Get all id's in CSV
csv_product_ids = []
with open("new_product_feed.csv", 'r') as csvfile:
    linecount = 0
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        linecount += 1
        csv_product_ids.append(int(row['aw_product_id']))
    print("{0} rows in CSV ids".format(linecount))

# Get all id's in the Database
db_product_ids = [int(product.aw_product_id) for product in Product.objects.all()]

matching_ids = set(csv_product_ids).intersection(db_product_ids)

# If a CSV id is not in the products id, then import
importIds = []
for csv_id in csv_product_ids:
    if csv_id not in db_product_ids:
        importIds.append(int(csv_id))

# If a product id is not in the csv id, then delete
def deleteProducts():
    linecount = 0
    for product_id in db_product_ids:
        if product_id not in csv_product_ids:
            linecount += 1
            Product.objects.filter(id=product_id).delete()
    print("Deleted {0} products".format(linecount))

def updateProducts():
    with open("new_product_feed.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        linecount = 0
        for row in reader:
            if int(row['aw_product_id']) in matching_ids:
                linecount += 1
                Brand.objects.filter(id=int(row['aw_product_id'])).update(brand_name=row['brand_name'])
                Product.objects.filter(id=int(row['aw_product_id'])).update(
                    aw_deep_link=row['aw_deep_link'],
                    description=row['description'],
                    product_name=row['product_name'],
                    aw_image_url=row['aw_image_url'],
                    search_price=row['search_price'],
                    merchant_name=row['merchant_name'],
                    display_price=row['display_price'],
                    colour=row['colour'],
                    rrp_price=row['rrp_price'],
                    size=row['Fashion:size']
                )
        print("Updated {0} products".format(linecount))

def importProducts():
    all_categories = list(Category.objects.all())
    with open('new_product_feed.csv') as f:
        linecount = 0
        next(f)
        for line in f:
            fields = line.split(';')
            if int(fields[13]) in importIds:
                linecount += 1
                category = Category.objects.get_or_create(name=fields[11])
                brand_name = Brand.objects.get_or_create(brand_name=fields[8])

                data = {
                    'aw_deep_link': fields[1],
                    'description': fields[2],
                    'product_name': fields[3],
                    'aw_image_url': fields[4],
                    'search_price': fields[5],
                    'merchant_name': fields[6],
                    'display_price': fields[7],
                    'brand_name': brand_name[0],
                    'colour': fields[9],
                    'rrp_price': fields[10],
                    'category': category[0],
                    'size': fields[12],
                    'aw_product_id': fields[13]
                }

                for textfield in ('description', 'product_name'):
                    subcat = None
                    for cat in all_categories:
                        if re.search(cat.regex, data[textfield], re.IGNORECASE) is not None:
                            if cat.is_child_node():
                                subcat = cat

                    if subcat is not None:
                        break
                if subcat is not None:
                    data['category'] = subcat

                product = Product(**data)
                product.save()
        print("Imported {0} products".format(linecount))


deleteProducts()
updateProducts()
importProducts()

