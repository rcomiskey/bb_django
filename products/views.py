from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import django_filters
from .filters import ProductFilter

    
def view_products(request,hierarchy= None):
    category_slug = hierarchy.split('/')
    parent = None
    root = Category.objects.all()
    

    for slug in category_slug[:-1]:
        parent = root.get(parent=parent, slug = slug)
        

    try:
        product = Category.objects.get(parent=parent,slug=category_slug[-1])
        filter = ProductFilter(request.GET, queryset=Category.get_all_products(product))
    except:
        product = get_object_or_404(Product, slug = category_slug[-1])
        filter = ProductFilter(request.GET, queryset=Category.get_all_products(product))
        return render(request, "view_products.html", {'product': product, 'filter': filter })
    else:
        return render(request, 'view_products.html', {'product': product, 'filter': filter })
        

    

        