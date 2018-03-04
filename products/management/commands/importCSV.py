import re
from products.models import Category, Brand, Colour, Size
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Load some sample data into the db"
    
    def add_arguments(self, parser):
        parser.add_argument('--file', dest='file', help='File to load')

    
    def handle(self, **options):
        from products.models import Product, Category
        all_categories = list(Category.objects.all())
        

        
        if options['file']:
            print("Importing " + options['file'])
            
            with open(options['file']) as f:
                linecount = 0
                next(f)
                for line in f:
                    linecount += 1
                    fields = line.split(';')
                    category = Category.objects.get_or_create(name=fields[10])
                    brand_name = Brand.objects.get_or_create(brand_name=fields[7])
                    colour = Colour.objects.get_or_create(colour=fields[8])
                    size = Size.objects.get_or_create(size=fields[11])
                    
                    data = {
                            'aw_deep_link':  fields[0],
                            'description': fields[1],
                            'product_name': fields[2],
                            'aw_image_url':  fields[3],
                            'search_price':  fields[4],
                            'merchant_name': fields[5],
                            'display_price':  fields[6],
                            'brand_name':  brand_name[0],
                            'colour' :  colour[0],
                            'rrp_price' :  fields[9],
                            'category' :  category[0],
                            'slug' :  category[0],
                            'size':  size[0],
                            
                            
                    }
                    
                    
                    for textfield in ('description', 'product_name'):
                        subcat = None
                        for cat in all_categories:
                            if re.search(cat.regex, data[textfield]) is not None:
                                if cat.is_child_node():
                                    subcat = cat
            
                        if subcat is not None:
                            break
                    if subcat is not None:
                        data['category'] = subcat
                        
                    product = Product(**data)
                    product.save()

                print("Added {0} products".format(linecount))