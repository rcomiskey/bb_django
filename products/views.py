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
    total = len(filters.qs)
    page = request.GET.get('page')
    paginator = Paginator(filters.qs, 100)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, "view_products.html", {'product': product, 'filter': filters, 'currency': currency, 'products': products, 'total': total })

    # try:
    #     product = Category.objects.get(parent=parent,slug=category_slug[-1])
    #     filter = ProductFilter(request.GET, queryset=Category.get_all_products(product))
    # except:
    #     product = get_object_or_404(Product, slug = category_slug[-1])
    #     filter = ProductFilter(request.GET, queryset=Category.get_all_products(product))
    #     return render(request, "view_products.html", {'product': product, 'filter': filter, 'currency': currency })
    # else:
    #     return render(request, 'view_products.html', {'product': product, 'filter': filter, 'currency': currency })



import urllib.parse as urlparse
def do_search(request):
    currency = '€'
    # url = request.META.get('HTTP_REFERER')
    # print(url)
    # print(request.GET.get('q'))
    # if request.GET.get('q') != None:
    #     print(request.GET['q'])
    #     q = request.GET['q']
    # elif url != None:
    #     print(url)
    #     parsed = urlparse.urlparse(url)
    #     print(parsed)
    #     if urlparse.parse_qs(parsed.query)['q'] != None:
    #         print(urlparse.parse_qs(parsed.query)['q'])
    #
    #         q = 'nike'
    # else:
    #     q = 'nike'
    # q = 'nike'
    # print('hello')
    # print(url)
    product = Product.objects.filter(search_vector=request.GET['q'])
    filters = ProductFilter(request.GET, queryset=product)
    total = len(filters.qs)
    page = request.GET.get('page')
    paginator = Paginator(filters.qs, 20)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, "view_products_search.html", {'product': product, 'filter': filters, 'currency': currency, 'products': products, 'total': total })

def view_product_item(request, id):
    this_product = get_object_or_404(Product, id=id)
    this_product.save()
    currency = '€'
    promotions = Promotion.objects.filter(merchant__name__icontains=this_product.merchant_name)
    return render(request, "view_product_item.html", {'product': this_product, 'currency': currency, 'promotions': promotions})





