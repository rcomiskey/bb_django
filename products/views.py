from django.shortcuts import render
from .models import Product

def view_products(request):
    products = Product.objects.get_queryset().order_by('id')
    return render(request, 'view_products.html', {'products': products })
    

