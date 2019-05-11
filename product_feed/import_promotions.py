import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "best_bargain_project.settings")
django.setup()
from promotions.models import Promotion, Merchant, PromoType, MerchantCategory
import csv
import re
import urllib.request
import io
import gzip
import pandas
from django.contrib.postgres.search import SearchVector

# Read in CSV list from Awin
feed = pandas.read_csv('https://ui.awin.com/export-promotions/305691/2ce413d743fd334450d95af7d64217d3?downloadType=csv&promotionType=&categoryIds=&regionIds=&advertiserIds=&membershipStatus=joined&promotionStatus=')
feed.to_csv('promotion_feed_list.csv')

# Rearrange columns
header = [
    'Advertiser',
    'Title',
    'Description',
    'Type',
    'Starts',
    'Ends',
    'Deeplink',
    'Promotion ID',
    'Advertiser ID'
]

df = pandas.read_csv('promotion_feed_list.csv', sep=',')
df.to_csv('new_promotion_feed_list.csv', columns=header, sep=';')


def importPromotions():
    with open('new_promotion_feed_list.csv', encoding='utf8', errors='ignore') as f:
        linecount = 0
        next(f)
        for line in f:
            fields = line.split(';')
            linecount += 1
            # category = MerchantCategory.objects.get_or_create(category='')
            # merchant = Merchant.objects.get_or_create(name=fields[1], merchant_id=fields[9], category=category[0])
            merchant = Merchant.objects.get_or_create(name=fields[1], merchant_id=fields[9])
            promo_type = PromoType.objects.get_or_create(name=fields[4])
            # category = MerchantCategory.objects.get_or_create(category_id=)
            print(MerchantCategory.objects.filter(merchant_id=fields[9]))
            data = {
                'merchant': merchant[0],
                'title': fields[2],
                'description': fields[3],
                'promo_type': promo_type[0],
                'start_date': fields[5],
                'end_date': fields[6],
                'deeplink': fields[7],
                'promo_id': fields[8],
                # 'category': category
            }

            promotion = Promotion(**data)
            promotion.save()
    print("Imported {0} promotions".format(linecount))



importPromotions()
