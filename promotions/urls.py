from django.urls import re_path
from .views import getpromotions

urlpatterns = [
    re_path(r'^$', getpromotions,  name='getpromotions'),
]
