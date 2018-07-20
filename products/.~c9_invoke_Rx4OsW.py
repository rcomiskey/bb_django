import django_filters 
from .models import Product, Brand, Category, Size, Colour,  COLOURS, COLOURS2
from django.forms import CheckboxSelectMultiple
from django.db.models import Q
from django.db.models import Func, F
# Product.objects.annotate(abs_calculation=Func(Product.search_price < Product.rrp_price function='ABS').filter(abs_calculation)


COLOURS = (
('red' ,'Red'),
('blue' ,'Blue'),
)
# Company.objects.annotate(num_offerings=Count(F('products') + F('services')))
    
# def Colours(request, colour):
#     if "red" in colour:
blue = Colour.objects.filter(colour="blue")

COLOUR3 = {}
for variations, colour in COLOURS2:
    COLOUR3[colour] = [x.id for x in Colour.objects.filter(colour__in=variations)]

print(COLOUR3)

    
class ProductFilter(django_filters.FilterSet):
    search_price__gt = django_filters.NumberFilter(name='search_price', lookup_expr='gt', )
    search_price__lt = django_filters.NumberFilter(name='search_price', lookup_expr='lt')
    brand_name = django_filters.filters.ModelMultipleChoiceFilter( label='Brand',widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}), queryset = Brand.objects.all())
    colour = django_filters.filters.MultipleChoiceFilter(label='Colour', choices=COLOURS,widget=CheckboxSelectMultiple,method='filter_colour')
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
        return queryset.filter(colour__in=colour_ids)

    class Meta:
        model = Product
        fields = [ 'brand_name', 'colour']
        
        # def a(self, queryset, value):
        #     return queryset.filter(product_name=value)
        
        
   
   

        
        
        
        
      