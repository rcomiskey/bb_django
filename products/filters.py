import django_filters 
from .models import Product, Brand, Category, Colour, Size
from django.forms import CheckboxSelectMultiple


class ProductFilter(django_filters.FilterSet):
    search_price__gt = django_filters.NumberFilter(name='search_price', lookup_expr='gt')
    search_price__lt = django_filters.NumberFilter(name='search_price', lookup_expr='lt')
    brand_name = django_filters.filters.ModelMultipleChoiceFilter( label='Brand',widget=CheckboxSelectMultiple, queryset = Brand.objects.all())
    colour = django_filters.filters.ModelMultipleChoiceFilter( label='Colour',widget=CheckboxSelectMultiple, queryset = Colour.objects.all())
    size = django_filters.filters.ModelMultipleChoiceFilter( label='Size',widget=CheckboxSelectMultiple, queryset = Size.objects.all())
    
    class Meta:
        model = Product
        fields = ['brand_name', 'colour', 'size']
        
        
        
      