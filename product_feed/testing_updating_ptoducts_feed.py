import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "best_bargain_project.settings")
django.setup()
from products.models import Product
import csv

csv_product_ids = []
with open("product_feed.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        csv_product_ids.append(row['aw_product_id'])

print(csv_product_ids)

db_product_ids = [product.id for product in Product.objects.all()]
print(db_product_ids)

# ids that exist in both, update
b = [1,2,3,4,5,6,7, 2345234534, 435345134515]
def compare_intersect(x, y):
    return set(x).intersection(y)

a = compare_intersect(b, db_product_ids)
print(a)

# If a CSV id is not in the products id, then import
for csv_id in b:
    if csv_id not in db_product_ids:
        print(csv_id)

# If a product id is not in the csv id, then delete
for product_id in db_product_ids:
    if product_id not in b:
        print(product_id)


# 1. If the csv has id's that aren't in the db - keep
# 2. If the csv has id's that are in the db - update
# 3. If the csv doesn't have the id and the db does - delete


#
# search_prices = [product.search_price for product in Product.objects.all()]
# rrp_prices = [product.rrp_price for product in Product.objects.all()]
#
# SALE2 = []
# SALE3 = []
#
#
# for i in range(len(ids)-1):
#     if search_prices[i] < rrp_prices[i]:
#         SALE2.append(ids[i])
#     else:
#         SALE3.append(ids[i])
#
# print(SALE2)