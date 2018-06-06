import django_filters 
from .models import Promotion, Merchant, MerchantCategory
from django.forms import CheckboxSelectMultiple

class PromotionFilter(django_filters.FilterSet):
    merchant = django_filters.filters.ModelMultipleChoiceFilter( label='Merchant',widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}), queryset = Merchant.objects.all())
    promo_type = django_filters.filters.ModelMultipleChoiceFilter( label='Type',widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}), queryset = Promotion.objects.all())
    category = django_filters.filters.ModelMultipleChoiceFilter( label='Type',widget=CheckboxSelectMultiple(attrs={'class': 'check-label'}), queryset = MerchantCategory.objects.all())
    
    class Meta:
        model = Promotion
        fields = ['merchant']
        
   

        