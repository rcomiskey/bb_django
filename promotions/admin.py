from django.contrib import admin
from .models import Promotion, Merchant, MerchantCategory, PromoType


admin.site.register(Promotion)
admin.site.register(Merchant)
admin.site.register(MerchantCategory)
admin.site.register(PromoType)


        