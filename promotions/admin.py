from django.contrib import admin
from .models import Promotion, Merchant, PromoType, MerchantCategory


admin.site.register(Promotion)
admin.site.register(Merchant)
admin.site.register(PromoType)
admin.site.register(MerchantCategory)


        