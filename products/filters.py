import django_filters 
from .models import Product, Brand, Category, Size, Colour
from django.forms import CheckboxSelectMultiple
from django.db.models import Q



colours = [('grey', 'red'),('blue', 'blue')]
    
class ProductFilter(django_filters.FilterSet):
    search_price__gt = django_filters.NumberFilter(name='search_price', lookup_expr='gt', )
    search_price__lt = django_filters.NumberFilter(name='search_price', lookup_expr='lt')
    brand_name = django_filters.filters.ModelMultipleChoiceFilter( label='Brand',widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}), queryset = Brand.objects.all())
    # colour = django_filters.filters.MultipleChoiceFilter(label='Colour', choices=Colour.COLOURS,widget=CheckboxSelectMultiple)
    size = django_filters.filters.ModelMultipleChoiceFilter( label='Size',widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}), queryset = Size.objects.all())
    # sale = django_filters.filters.ModelMultipleChoiceFilter( label='Sale',widget=CheckboxSelectMultiple, queryset = Product.test.get_queryset())
    # product_name = django_filters.CharFilter(lookup_expr='icontains')
    # colour = django_filters.filters.CharFilter(lookup_expr='icontains')
    # size = django_filters.filters.CharFilter(lookup_expr='icontains')
    # colour = django_filters.MultipleChoiceFilter(choices=colours, lookup_expr='icontains')
    colour = django_filters.AllValuesMultipleFilter(widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}))
    
    
    class Meta:
        model = Product
        fields = [ 'brand_name']
        
   
   

        
        
        
        
      