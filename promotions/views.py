from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Promotion, Merchant
from django.utils import timezone
from django.conf import settings
from django.contrib import messages


# Create your views here.
def getpromotions(request):
   promotions = Promotion.objects.all()
   merchants = Merchant.objects.all()
   return render(request, "promotions.html", {'promotions': promotions, 'merchants': merchants})
   