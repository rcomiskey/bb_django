from django.contrib import admin
from .models import Product, Category, Brand
from mptt.admin import MPTTModelAdmin


admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category , MPTTModelAdmin) 

        




