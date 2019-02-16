from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import django_filters
from .filters import ProductFilter
from promotions.models import Promotion
from django.db.models import Q
import operator
from functools import reduce
import re


def view_products(request, hierarchy=None):
    currency = '€'
    category_slug = hierarchy.split('/')
    parent = None
    root = Category.objects.all()
    for slug in category_slug[:-1]:
        parent = root.get(parent=parent, slug = slug)
    product = Category.objects.get(parent=parent,slug=category_slug[-1])
    filters = ProductFilter(request.GET, queryset=Category.get_all_products(product))
    page = request.GET.get('page')
    paginator = Paginator(filters.qs, 20)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, "view_products.html", {'product': product, 'filter': filters, 'currency': currency, 'products': products })

    # try:
    #     product = Category.objects.get(parent=parent,slug=category_slug[-1])
    #     filter = ProductFilter(request.GET, queryset=Category.get_all_products(product))
    # except:
    #     product = get_object_or_404(Product, slug = category_slug[-1])
    #     filter = ProductFilter(request.GET, queryset=Category.get_all_products(product))
    #     return render(request, "view_products.html", {'product': product, 'filter': filter, 'currency': currency })
    # else:
    #     return render(request, 'view_products.html', {'product': product, 'filter': filter, 'currency': currency })




def do_search(request):
    currency = '€'
    product = Product.objects.filter(search_vector=request.GET['q'])
    filters = ProductFilter(request.GET, queryset=product)
    page = request.GET.get('page')
    paginator = Paginator(filters.qs, 20)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, "view_products.html", {'product': product, 'filter': filters, 'currency': currency, 'products': products })

def view_product_item(request, id):
    this_product = get_object_or_404(Product, id=id)
    this_product.save()
    currency = '€'
    promotions = Promotion.objects.filter(merchant__name__icontains=this_product.merchant_name)
    return render(request, "view_product_item.html", {'product': this_product, 'currency': currency, 'promotions': promotions})





