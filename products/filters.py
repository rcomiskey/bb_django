import django_filters
from .models import Product, Brand, Category, Merchant
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
    (('beige', 'bg'), 'beige'),
    (('black', 'blck'), 'black'),
    (('blue', 'denim', 'teal', 'royal'),'blue'),
    (('brown', 'brwn', 'bronze', 'tan'),'brown'),
    (('gold', 'gld'), 'gold'),
    (('green', 'grn', 'kamo', 'camo', 'khaki', 'lime', 'mint', 'olive', 'turquoise'), 'green'),
    (('grey', 'gray', 'gry', 'charcoal', 'stone'), 'grey'),
    (('navy', 'nvy'), 'navy'),
    (('nude', 'skin'), 'nude'),
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
        clauses = (Q(colour__iexact=p) for p in variations)
    else:
        clauses = (Q(colour__icontains=p) for p in variations)
    query = reduce(operator.or_, clauses)
    COLOUR3[colour] = [x.id for x in Product.objects.filter(query)]

CLOTHING_SIZES = (
    ('extra extra small', 'Extra Extra Small'),
    ('extra small', 'Extra Small'),
    ('small', 'Small'),
    ('medium', 'Medium'),
    ('large', 'Large'),
    ('extra Large', 'Extra Large'),
    ('extra extra large', 'Extra Extra Large')
    )

CLOTHING_SIZES2 = (
    (('(?:^|\W)xxs(?:$|\W)', '(?=.*small)(extra.*){2}'), 'extra extra small'),
    (('(?:^|\W)xs(?:$|\W)', '^extra small$'), 'extra small'),
    (('(?:^|\W)s(?:$|\W)', '^(?!.*extra).*small.*$'), 'small'),
    (('(?:^|\W)m(?:$|\W)', '^(?!.*extra).*medium.*$'), 'medium'),
    (('(?:^|\W)l(?:$|\W)', '^(?!.*extra).*large.*$'), 'large'),
    (('(?:^|\W)xl(?:$|\W)', '^extra large$'), 'extra Large'),
    (('(?:^|\W)xxl(?:$|\W)', '(?=.*large)(extra.*){2}'), 'extra extra large')
    )

CLOTHING_SIZES3 = {}
for variations, size in CLOTHING_SIZES2:
    clauses = (Q(size__iregex=p) for p in variations)
    query = reduce(operator.or_, clauses)
    CLOTHING_SIZES3[size] = [x.id for x in Product.objects.filter(query)]


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

# (?:^|\W)1(?:$|\W)
# matches number without have another numerical number around it
SIZES3 = {}
for variations, size in SIZES2:
    clauses = (Q(size__iregex='(?:^|\W)' + p + '(?:$|\W)') for p in variations)
    query = reduce(operator.or_, clauses)
    SIZES3[size] = [x.id for x in Product.objects.filter(query)]
#     print(query)
# print(SIZES3)


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
    brand_name = django_filters.filters.ModelMultipleChoiceFilter( label='Brand',widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}), queryset=Brand.objects.all().order_by('brand_name'))
    colour = django_filters.filters.MultipleChoiceFilter(label='Colour', choices=COLOURS, widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}), method='filter_colour')
    size = django_filters.filters.MultipleChoiceFilter(label='Size', choices=SIZES, widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}), method='filter_size')
    clothing_size = django_filters.filters.MultipleChoiceFilter(label='Clothing Size', choices=CLOTHING_SIZES, widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}), method='filter_clothing_size')
    merchant_name = django_filters.filters.ModelMultipleChoiceFilter(label='Shop', widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}), queryset=Merchant.objects.all().order_by('merchant_name'))
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

    def filter_clothing_size(self, queryset, name, value):
        # construct the full lookup expression.
        clothing_size_ids = []
        for clothing_size in value:
            clothing_size_ids.extend(CLOTHING_SIZES3[clothing_size])
        return queryset.filter(id__in=clothing_size_ids)


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










