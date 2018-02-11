from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import django_filters
from .filters import ProductFilter

# def view_products(request):
#     products = Product.objects.get_queryset().order_by('id')
#     return render(request, 'view_products.html', {'products': products })
    
def view_products(request,hierarchy= None):
    category_slug = hierarchy.split('/')
    parent = None
    root = Category.objects.all()

    for slug in category_slug[:-1]:
        parent = root.get(parent=parent, slug = slug)

    try:
        product = Category.objects.get(parent=parent,slug=category_slug[-1])
    except:
        product = get_object_or_404(Product, slug = category_slug[-1])
        return render(request, "view_products.html", {'product': product})
    else:
        return render(request, 'view_products.html', {'product': product})
        
        
def product_list(request):
    f = ProductFilter(request.GET, queryset=Product.objects.all())
    return render(request, 'template.html', {'filter': f})
        