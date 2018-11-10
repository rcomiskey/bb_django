import django_filters 
from .models import Product, Brand, Category
from django.forms import CheckboxSelectMultiple, RadioSelect
from django.db.models import Q
from django.db.models import Func, F
import operator
from functools import reduce


COLOURS = (
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
    ('white' ,'White'),
    ('yellow', 'Yellow'),
    )

COLOURS2 = (
    (('beige','bg'), 'beige'),
    (('black', 'blck'),'black'),
    (('blue', 'denim', 'teal', 'royal'),'blue'),
    (('brown', 'brwn', 'bronze'),'brown'),
    (('gold', 'gld'), 'gold'),
    (('green', 'grn', 'kamo', 'camo', 'khaki', 'lime', 'mint', 'olive', 'turquoise'), 'green'),
    (('grey', 'gray', 'gry', 'charcoal', 'stone'), 'grey'),
    (('navy', 'nvy'), 'navy'),
    (('nude'), 'nude'),
    (('orange', 'orng', 'apricot'), 'orange'),
    (('pink', 'pnk'), 'pink'),
    (('purple', 'purpl', 'burgundy'), 'purple'),
    (('red', 'rd'), 'red'),
    (('silver', 'slvr'), 'silver'),
    (('white', 'wht'), 'white'),
    (('yellow', 'yllw'), 'yellow'),
    )

COLOUR3 = {}
for variations, colour in COLOURS2:
    if colour == 'white':
        clauses = (Q(colour=p) for p in variations)
    else:
        clauses = (Q(colour__icontains=p) for p in variations)
    query = reduce(operator.or_, clauses)
    COLOUR3[colour] = [x.id for x in Product.objects.filter(query)]

SIZES = (
    ('1', '1'),
    ('1.5', '1.5'),
    ('2','2'),
    ('2.5','2.5'),
    ('3','3'),
    ('3.5', '3.5'),
    ('4','4'),
    ('4.5','4.5'),
    ('5', '5'),
    ('5.5', '5.5'),
    ('6', '6'),
    ('6.5', '6.5'),
    ('7', '7'),
    ('7.5', '7.5'),
    ('8' ,'8'),
    ('8.5', '8.5'),
    ('9', '9'),
    ('9.5', '9.5'),
    ('10', '10'),
    ('10.5', '10.5'),
    ('11', '11'),
    ('11.5', '11.5'),
    ('12', '12'),
    ('12.5', '12.5'),
    ('13', '13'),
    )

SIZES2 = (
    (('1', '34'), '1'),
    (('1.5', '34.5') , '1.5'),
    (('2', '35'), '2'),
    (('2.5', '35.5'), '2.5'),
    (('3', '36'), '3'),
    (('3.5', '36.5'), '3.5'),
    (('4', '37'), '4'),
    (('4.5', '37.5'), '4.5'),
    (('5', '38'), '5'),
    (('5.5', '38.5'), '5.5'),
    (('6', '39'), '6'),
    (('6.5', '39.5'), '6.5'),
    (('7', '40'), '7'),
    (('7.5', '40.5'), '7.5'),
    (('8', '41') ,'8'),
    (('8.5', '41.5'), '8.5'),
    (('9', '42'), '9'),
    (('9.5', '42.5'), '9.5'),
    (('10', '43'), '10'),
    (('10.5', '43.5'), '10.5'),
    (('11', '44'), '11'),
    (('11.5', '44.5'), '11.5'),
    (('12', '45'), '12'),
    (('12.5', '45.5'), '12.5'),
    (('13', '46'), '13'),
    )

SIZES3 = {}
for variations, size in SIZES2:
    clauses = (Q(size__icontains=p) for p in variations)
    query = reduce(operator.or_, clauses)
    SIZES3[size] = [x.id for x in Product.objects.filter(query)]
    print(query)
print(SIZES3)


SALE = (
    ('true', 'ON SALE'),
    ('false', 'NOT ON SALE'),
    )

ids = [product.id for product in Product.objects.all()]
search_prices = [product.search_price for product in Product.objects.all()]
rrp_prices = [product.rrp_price for product in Product.objects.all()]

SALE2 = []
SALE3 = []


for i in range(len(ids)-1):
    if search_prices[i] < rrp_prices[i]:
        SALE2.append(ids[i])
    else:
        SALE3.append(ids[i])

SORT = (
    ('low', 'LOW TO HIGH'),
    ('high', 'HIGH TO LOW'),
    )

class ProductFilter(django_filters.FilterSet):
    search_price__gt = django_filters.NumberFilter(name='search_price', lookup_expr='gt' )
    search_price__lt = django_filters.NumberFilter(name='search_price', lookup_expr='lt')
    brand_name = django_filters.filters.ModelMultipleChoiceFilter( label='Brand',widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}), queryset = Brand.objects.all().order_by('brand_name'))
    colour = django_filters.filters.MultipleChoiceFilter(label='Colour', choices=COLOURS, widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}), method='filter_colour')
    size = django_filters.filters.MultipleChoiceFilter(label='Size', choices=SIZES, widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}), method='filter_size')
    # # sale = django_filters.ModelMultipleChoiceFilter(queryset=Product.objects.annotate(on_sale=(F('rrp_price') - F('search_price'))
    # # product_name = django_filters.CharFilter(lookup_expr='icontains')
    # # colour = django_filters.filters.CharFilter()
    # # size = django_filters.filters.CharFilter(lookup_expr='icontains')
    # # red = django_filters.filters.ChoiceFilter(queryset=Colour.objects.filter(colour="red"),widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}))
    # # colour = django_filters.AllValuesMultipleFilter(label='Colour', widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}))
    product = Product.objects.all()
    sale = django_filters.filters.MultipleChoiceFilter(label='Sale', choices=SALE, widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}), method='filter_sale')
    sort = django_filters.filters.ChoiceFilter(label='Sort', choices=SORT, widget=RadioSelect(attrs={'class': 'check-label'}), method='filter_sort')


    def filter_colour(self, queryset, name, value):
        # construct the full lookup expression.
        colour_ids =  []
        # print(queryset)
        for colour in value:
            colour_ids.extend(COLOUR3[colour])
        # print(colour_ids)
        return queryset.filter(id__in=colour_ids)

    def filter_size(self, queryset, name, value):
        # construct the full lookup expression.
        size_ids = []
        for size in value:
            size_ids.extend(SIZES3[size])
        return queryset.filter(id__in=size_ids)


    def filter_sale(self, queryset, name, value):
        id_list = []
        for value in value:
            if value == 'true':
                id_list.extend(SALE2)
            else:
                id_list.extend(SALE3)
        return queryset.filter(id__in=id_list)

    def filter_sort(self, queryset, name, value):
        if value == 'low':
            return queryset.order_by('search_price')
        if value == 'high':
            return queryset.order_by('-search_price')



        
        
    class Meta:
        model = Product
        fields = [ 'brand_name', 'colour']

        
        







