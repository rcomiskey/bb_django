from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Promotion, Merchant
from django.utils import timezone
from django.conf import settings
from django.contrib import messages
from .filters import PromotionFilter


# Create your views here.
def getpromotions(request):
    promo_filter = PromotionFilter(request.GET, queryset=Promotion.objects.all())
    return render(request, "promotions.html", {'promo_filter': promo_filter})
   
def viewpromotion(request, id):
    this_promotion = get_object_or_404(Promotion, id=id)
    this_promotion.save()
    return render(request, "viewpromotion.html", {'promotion': this_promotion})
   