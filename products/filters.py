import django_filters 
from .models import Product, Brand, Category, Size,  COLOURS, COLOURS2
from django.forms import CheckboxSelectMultiple
from django.db.models import Q
from django.db.models import Func, F
import operator
from functools import reduce


# COLOURS = (
# ('red' ,'Red'),
# ('blue' ,'Blue'),
# )

COLOURS = (
    ('white' ,'White'),
    ('beige', 'Beige'),
    ('black', 'Black'),
    ('blue','Blue'),
    ('brown','Brown'),
    ('gold','gold'),
    ('green', 'Green'),
    ('grey','Grey'),
    ('navy','Navy'),
    ('nude', 'Nude'),
    ('orange', 'Orange'),
    ('pink', 'Pink'),
    ('purple', 'Purple'),
    ('red', 'Red'),
    ('silver', 'Silver'),
    ('yellow', 'Yellow'),
    )

COLOUR3 = {}
for variations, colour in COLOURS2:
    clauses = (Q(colour__icontains=p) for p in variations)
    query = reduce(operator.or_, clauses)
    COLOUR3[colour] = [x.id for x in Product.objects.filter(query)]

    
class ProductFilter(django_filters.FilterSet):
    search_price__gt = django_filters.NumberFilter(name='search_price', lookup_expr='gt', )
    search_price__lt = django_filters.NumberFilter(name='search_price', lookup_expr='lt')
    brand_name = django_filters.filters.ModelMultipleChoiceFilter( label='Brand',widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}), queryset = Brand.objects.all())
    colour = django_filters.filters.MultipleChoiceFilter(label='Colour', choices=COLOURS, widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}), method='filter_colour')
    size = django_filters.filters.ModelMultipleChoiceFilter( label='Size',widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}), queryset = Size.objects.all())
    # sale = django_filters.ModelMultipleChoiceFilter(queryset=Product.objects.annotate(on_sale=(F('rrp_price') - F('search_price'))
    # product_name = django_filters.CharFilter(lookup_expr='icontains')
    # colour = django_filters.filters.CharFilter()
    # size = django_filters.filters.CharFilter(lookup_expr='icontains')
    # red = django_filters.filters.ChoiceFilter(queryset=Colour.objects.filter(colour="red"),widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}))
    # colour = django_filters.AllValuesMultipleFilter(label='Colour', widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}))
    product = Product.objects.all()

    def filter_colour(self, queryset, name, value):
        # construct the full lookup expression.
        colour_ids =  []
        for colour in value:
            colour_ids.extend(COLOUR3[colour])
        return queryset.filter(id__in=colour_ids)

    class Meta:
        model = Product
        fields = [ 'brand_name', 'colour']

        
        
   
   

        
        
        
        
      