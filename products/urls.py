from .views import view_products, do_search
from django.urls import re_path


urlpatterns = [
    re_path(r'^category/(?P<hierarchy>.+)/$', view_products, name='view_products'),
    re_path(r'^search', do_search, name='search')
    ]