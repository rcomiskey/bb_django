from django.contrib import admin
from .models import Product, Category, Brand, Colour, Size
from mptt.admin import MPTTModelAdmin


admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Colour)
admin.site.register(Size)
admin.site.register(Category , MPTTModelAdmin) 

        




