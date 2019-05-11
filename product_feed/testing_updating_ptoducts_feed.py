import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "best_bargain_project.settings")
django.setup()
from products.models import Product, Category, Brand, Merchant
import csv
import re
import urllib.request
import io
import gzip
import pandas
from django.contrib.postgres.search import SearchVector

# Read in CSV list from Awin
feed = pandas.read_csv('https://productdata.awin.com/datafeed/list/apikey/c43cb2adc7d4b494d4d5ef358ef0050d')
feed.to_csv('product_feed_list.csv')

# , '2165', '2374', '4412', '6518', '5374'
advertisersUrls = {
'2606': 'https://productdata.awin.com/datafeed/download/apikey/c43cb2adc7d4b494d4d5ef358ef0050d/language/en/fid/2606/columns/aw_deep_link,product_name,aw_product_id,merchant_product_id,merchant_image_url,description,merchant_category,search_price,merchant_name,category_name,currency,merchant_deep_link,brand_name,colour,rrp_price,mpn/format/csv/delimiter/%2C/compression/gzip/adultcontent/1/',
'2165': 'https://productdata.awin.com/datafeed/download/apikey/c43cb2adc7d4b494d4d5ef358ef0050d/language/en/fid/2165/columns/aw_deep_link,product_name,aw_product_id,merchant_product_id,merchant_image_url,description,merchant_category,search_price,merchant_name,category_name,aw_image_url,merchant_deep_link,brand_name,specifications,rrp_price,currency,in_stock/format/csv/delimiter/%3B/compression/gzip/adultcontent/1/',
'2374': 'https://productdata.awin.com/datafeed/download/apikey/c43cb2adc7d4b494d4d5ef358ef0050d/language/en/fid/12433/columns/aw_deep_link,product_name,aw_product_id,merchant_product_id,merchant_image_url,description,merchant_category,search_price,merchant_name,category_name,currency,brand_name,colour,rrp_price,Fashion%3Asize/format/csv/delimiter/%7C/compression/gzip/adultcontent/1/',
'4412': 'https://productdata.awin.com/datafeed/download/apikey/c43cb2adc7d4b494d4d5ef358ef0050d/language/en/fid/4412/columns/aw_deep_link,product_name,aw_product_id,merchant_product_id,merchant_image_url,description,merchant_category,search_price,merchant_name,category_name,aw_image_url,currency,brand_name,colour,dimensions,rrp_price/format/csv/delimiter/%3B/compression/gzip/adultcontent/1/',
'6518': 'https://productdata.awin.com/datafeed/download/apikey/c43cb2adc7d4b494d4d5ef358ef0050d/language/en/fid/12161,18325/columns/aw_deep_link,product_name,aw_product_id,merchant_product_id,merchant_image_url,description,merchant_category,search_price,merchant_name,currency,category_name,brand_name,colour,rrp_price,Fashion%3Asize/format/csv/delimiter/%3B/compression/gzip/adultcontent/1/',
'5374': 'https://productdata.awin.com/datafeed/download/apikey/c43cb2adc7d4b494d4d5ef358ef0050d/language/en/fid/17383/columns/aw_deep_link,product_name,aw_product_id,merchant_product_id,merchant_image_url,description,merchant_category,search_price,aw_image_url,currency,colour,merchant_name,category_name,rrp_price,Fashion%3Asize/format/csv/delimiter/%3B/compression/gzip/adultcontent/1/'

}
#
with open('product_feed_list.csv', 'r') as pf:
    linecount = 0
    reader = csv.DictReader(pf, delimiter=',')
    for line in reader:
        linecount += 1
        if line['Membership Status'] == 'active' and line['Advertiser ID'] in ['2606', '2165', '2374', '4412', '6518', '5374']:
            advertiserId = line['Advertiser ID']
            print(advertiserId)
            print(advertisersUrls[advertiserId])


            # Read in CSV from Awin
            response = urllib.request.urlopen(advertisersUrls[line['Advertiser ID']])
            compressed_file = io.BytesIO(response.read())
            decompressed_file = gzip.GzipFile(fileobj=compressed_file)

            with open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'product_feed/product_feed'), 'wb') as outfile:
                outfile.write(decompressed_file.read())

            # Remove quotes
            with open('product_feed', 'r', encoding='utf8', errors='ignore') as f, open('product_feed.csv', 'w', encoding='utf8', errors='ignore') as fo:
                linecount = 0
                for line in f:
                    linecount += 1
                    fo.write(line.replace('"', '').replace("'", ""))
                print("{0} rows in CSV".format(linecount))

            # Rearrange columns
            if advertiserId == '2606':
                merchantName = 'M and M Direct IE'
                print(merchantName)
                delimiter = ','
                header = [
                    'aw_deep_link',
                    'description',
                    'product_name',
                    'merchant_image_url',
                    'search_price',
                    'merchant_name',
                    'brand_name',
                    'colour',
                    'rrp_price',
                    'category_name',
                    'mpn',
                    'aw_product_id',
                    'currency'
                ]
            elif advertiserId == '2165':
                merchantName = 'Schuh Ireland'
                print(merchantName)
                delimiter = ';'
                header = [
                    'aw_deep_link',
                    'description',
                    'product_name',
                    'merchant_image_url',
                    'search_price',
                    'merchant_name',
                    'brand_name',
                    'specifications',
                    'rrp_price',
                    'category_name',
                    'in_stock',
                    'aw_product_id',
                    'currency'
                ]
            elif advertiserId == '6518':
                merchantName = 'Pretty Little Thing IE'
                print(merchantName)
                delimiter = ';'
                header = [
                    'aw_deep_link',
                    'description',
                    'product_name',
                    'merchant_image_url',
                    'search_price',
                    'merchant_name',
                    'brand_name',
                    'colour',
                    'rrp_price',
                    'category_name',
                    'Fashion:size',
                    'aw_product_id',
                    'currency'
                ]
            elif advertiserId == '2374':
                merchantName = 'Office Shoes'
                print(merchantName)
                delimiter = '|'
                header = [
                    'aw_deep_link',
                    'description',
                    'product_name',
                    'merchant_image_url',
                    'search_price',
                    'merchant_name',
                    'brand_name',
                    'colour',
                    'rrp_price',
                    'category_name',
                    'Fashion:size',
                    'aw_product_id',
                    'currency'
                ]
            elif advertiserId == '5374':
                merchantName = 'SportsDirect.com'
                print(merchantName)
                delimiter = ';'
                header = [
                    'aw_deep_link',
                    'description',
                    'product_name',
                    'merchant_image_url',
                    'search_price',
                    'merchant_name',
                    'brand_name',
                    'colour',
                    'rrp_price',
                    'category_name',
                    'Fashion:size',
                    'aw_product_id',
                    'currency'
                ]
            elif advertiserId == '4412':
                merchantName = 'Superdry UK'
                print(merchantName)
                delimiter = ';'
                header = [
                    'aw_deep_link',
                    'description',
                    'product_name',
                    'merchant_image_url',
                    'search_price',
                    'merchant_name',
                    'brand_name',
                    'colour',
                    'rrp_price',
                    'category_name',
                    'dimensions',
                    'aw_product_id',
                    'currency'
                ]
            else:
                header = [
                    'aw_deep_link',
                    'description',
                    'product_name',
                    'merchant_image_url',
                    'search_price',
                    'merchant_name',
                    'brand_name',
                    'colour',
                    'rrp_price',
                    'category_name',
                    'Fashion:size',
                    'aw_product_id',
                    'currency'
                ]
            df = pandas.read_csv('product_feed.csv', sep=delimiter, error_bad_lines=False)
            df.to_csv('new_product_feed.csv', columns=header, sep=delimiter)

            # Get all id's in CSV
            csv_product_ids = []
            with open("new_product_feed.csv", 'r', encoding='utf8', errors='ignore') as csvfile:
                linecount = 0
                reader = csv.DictReader(csvfile, delimiter=delimiter)
                for row in reader:
                    linecount += 1
                    csv_product_ids.append(int(row['aw_product_id']))
                print("{0} rows in CSV ids".format(linecount))

            # Get all id's in the Database
            db_product_ids = [int(product.aw_product_id) for product in Product.objects.filter(merchant_name__merchant_name=merchantName)]

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
                with open("new_product_feed.csv", 'r', encoding='utf8', errors='ignore') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=delimiter)
                    linecount = 0
                    for row in reader:
                        if int(row['aw_product_id']) in matching_ids:
                            linecount += 1
                            Brand.objects.filter(id=int(row['aw_product_id'])).update(brand_name=row['brand_name'])
                            Merchant.objects.filter(id=int(row['aw_product_id'])).update(merchant_name=row['merchant_name'])
                            Product.objects.filter(id=int(row['aw_product_id'])).update(
                                aw_deep_link=row[header[0]],
                                description=row[header[1]],
                                product_name=row[header[2]],
                                aw_image_url=row[header[3]],
                                search_price=row[header[4]],
                                colour=row[header[7]],
                                rrp_price=row[header[8]],
                                size=row[header[10]],
                                currency=row[header[12]]
                            )
                    print("Updated {0} products".format(linecount))

            def importProducts():
                all_categories = list(Category.objects.all())
                with open('new_product_feed.csv', encoding='utf8', errors='ignore') as f:
                    linecount = 0
                    next(f)
                    for line in f:
                        fields = line.split(delimiter)
                        if int(fields[12]) in importIds:
                            linecount += 1
                            category = Category.objects.get_or_create(name=fields[10])
                            brand_name = Brand.objects.get_or_create(brand_name=fields[7].lower())
                            merchant_name = Merchant.objects.get_or_create(merchant_name=fields[6])
                            search_vector = SearchVector('description', 'product_name')
                            Product.objects.update(search_vector=search_vector)
                            # " ".join((fields[2].replace(":", ""), fields[3], fields[6], fields[7], fields[8]))

                            data = {
                                'aw_deep_link': fields[1],
                                'description': fields[2],
                                'product_name': fields[3],
                                'aw_image_url': fields[4],
                                'search_price': fields[5],
                                'merchant_name': merchant_name[0],
                                'brand_name': brand_name[0],
                                'colour': fields[8],
                                'rrp_price': fields[9],
                                'category': category[0],
                                'size': fields[11],
                                'aw_product_id': fields[12],
                                'currency': fields[13]
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


            # deleteProducts()
            # updateProducts()
            importProducts()

