from django.urls import re_path
from .views import getposts, viewpost, addcomment

urlpatterns = [
    re_path(r'^$', getposts,  name='getposts'),
    re_path(r'^(?P<slug>[-\w\d]+)/$', viewpost,  name='viewpost'),
    re_path(r'^(.+)/comments/add$', addcomment,  name='addcomment'),
]
