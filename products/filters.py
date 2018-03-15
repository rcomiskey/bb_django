import django_filters 
from .models import Product, Brand, Category, Size, COLOURS
from django.forms import CheckboxSelectMultiple


    
class ProductFilter(django_filters.FilterSet):
    search_price__gt = django_filters.NumberFilter(name='search_price', lookup_expr='gt')
    search_price__lt = django_filters.NumberFilter(name='search_price', lookup_expr='lt')
    brand_name = django_filters.filters.ModelMultipleChoiceFilter( label='Brand',widget=CheckboxSelectMultiple, queryset = Brand.objects.all())
    # colour = django_filters.filters.ModelMultipleChoiceFilter(label='Colour',widget=CheckboxSelectMultiple, queryset = Colour.objects.get_queryset())
    colour__exact = django_filters.filters.MultipleChoiceFilter(choices=COLOURS, widget=CheckboxSelectMultiple)
    size = django_filters.filters.ModelMultipleChoiceFilter( label='Size',widget=CheckboxSelectMultiple, queryset = Size.objects.filter(size__icontains='medium'))
    # sale = django_filters.filters.ModelMultipleChoiceFilter( label='Sale',widget=CheckboxSelectMultiple, queryset = Product.test.get_queryset())
    # product_name = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Product
        fields = ['colour', 'brand_name', 'size']
        
   

        
        
        
        
      