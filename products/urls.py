from .views import view_products
from django.urls import re_path


urlpatterns = [
    re_path('', view_products, name='view_products')
    ]