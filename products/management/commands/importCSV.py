import re
from products.models import Category, Brand
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Load some sample data into the db"
    
    def add_arguments(self, parser):
        parser.add_argument('--file', dest='file', help='File to load')

    
    def handle(self, **options):
        from products.models import Product, Category
        all_categories = list(Category.objects.all())
        # all_colours = list(Colour.objects.all())
       
    
        if options['file']:
            print("Importing " + options['file'])
            
            with open(options['file']) as f:
                linecount = 0
                next(f)
                for line in f:
                    linecount += 1
                    fields = line.split(';')
                    category = Category.objects.get_or_create(name=fields[11])
                    brand_name = Brand.objects.get_or_create(brand_name=fields[8])
                    # size = Size.objects.get_or_create(size=fields[12])
                    # colour = Colour.objects.get_or_create(colour=fields[8])
                    
                    data = {
                            'aw_deep_link':  fields[1],
                            'description': fields[2],
                            'product_name': fields[3],
                            'aw_image_url':  fields[4],
                            'search_price':  fields[5],
                            'merchant_name': fields[6],
                            'display_price':  fields[7],
                            'brand_name':  brand_name[0],
                            'colour':  fields[9],
                            'rrp_price':  fields[10],
                            'category':  category[0],
                            'size':  fields[12],
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
                        
                
                    
                    # for word in (colour):
                    #     print(word)
                    #     new = None
                    #     for item in all_colours:
                    #         if re.search(item.regex, str(word), re.IGNORECASE) is not None:
                    #             new = item
                    #     if new is not None:
                    #         break
                        
                    # if new is not None:
                        
                    #     data['colour'] = new
                        
                            
                
                    product = Product(**data)
                    product.save()

                print("Added {0} products".format(linecount))