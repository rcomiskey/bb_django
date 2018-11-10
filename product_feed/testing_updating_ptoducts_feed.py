import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "best_bargain_project.settings")
django.setup()
from products.models import Product, Category, Brand
import csv
import re

# Get all id's in CSV
csv_product_ids = []
with open("new_product_feed.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        csv_product_ids.append(int(row['aw_product_id']))

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
    for product_id in db_product_ids:
        if product_id not in csv_product_ids:
            Product.objects.filter(id=product_id).delete()

def updateProducts():
    with open("new_product_feed.csv", 'r') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            if int(row['aw_product_id']) in matching_ids:
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

def importProducts():
    all_categories = list(Category.objects.all())
    with open('new_product_feed.csv') as f:
        linecount = 0
        next(f)
        for line in f:
            fields = line.split(';')
            if fields[13] in importIds:
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
        print("Added {0} products".format(linecount))


deleteProducts()
updateProducts()
importProducts()

