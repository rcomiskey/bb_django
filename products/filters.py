import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    search_price__gt = django_filters.NumberFilter(name='search_price', lookup_expr='gt')
    search_price__lt = django_filters.NumberFilter(name='search_price', lookup_expr='lt')
    class Meta:
        model = Product
        fields = ['brand_name', 'category']
        # {
        #     'search_price': ['lt', 'gt'],
        #     'product_name': ['icontains'],
            
            
        # }