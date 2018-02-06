from .views import view_products
from django.urls import re_path


urlpatterns = [
    re_path(r'^category/(?P<hierarchy>.+)/$', view_products, name='view_products'),
    ]