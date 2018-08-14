from django.urls import re_path
from .views import getpromotions, viewpromotion

urlpatterns = [
    re_path(r'^$', getpromotions,  name='getpromotions'),
    re_path(r'^(\d+)$', viewpromotion,  name='viewpromotion')
]
