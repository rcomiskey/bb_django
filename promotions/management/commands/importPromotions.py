# import re
# from promotions.models import Promotion
# from django.core.management.base import BaseCommand
#
#
# class Command(BaseCommand):
#     help = "Import a csv with promotions"
#
#     def add_arguments(self, parser):
#         parser.add_argument('--file', dest='file', help='File to load')
#
#     def handle(self, **options):
#         # from products.models import Product, Category
#         # all_categories = list(Category.objects.all())
#         # all_colours = list(Colour.objects.all())
#
#         if options['file']:
#             print("Importing " + options['file'])
#
#             with open(options['file']) as f:
#                 linecount = 0
#                 next(f)
#                 for line in f:
#                     linecount += 1
#                     fields = line.split(';')
#                     # category = Category.objects.get_or_create(name=fields[10])
#                     # brand_name = Brand.objects.get_or_create(brand_name=fields[7])
#                     # size = Size.objects.get_or_create(size=fields[11])
#                     # # colour = Colour.objects.get_or_create(colour=fields[8])
#
#                     data = {
#                         'merchant': fields[0]
#                         # 'description': fields[1],
#                         # 'product_name': fields[2],
#                         # 'aw_image_url': fields[3],
#                         # 'search_price': fields[4],
#                         # 'merchant_name': fields[5],
#                         # 'display_price': fields[6],
#                         # 'brand_name': brand_name[0],
#                         # 'colour': fields[8],
#                         # 'rrp_price': fields[9],
#                         # 'category': category[0],
#                         # 'size': size[0],
#                     }
#
#                     promotion = Promotion(**data)
#                     promotion.save()
#
#                 print("Added {0} promotions".format(linecount))