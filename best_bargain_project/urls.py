"""best_bargain_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, re_path, path
from home.views import index, privacyPolicy, termsConditions
from products.views import do_search
from .settings import MEDIA_ROOT
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', index, name='index'),
    re_path(r'^terms-and-conditions$', termsConditions, name='termsConditions'),
    re_path(r'^privacy-and-cookie-policy$', privacyPolicy, name='privacyPolicy'),
    re_path(r'searchproducts', do_search, name='search'),
    re_path(r'^products/', include('products.urls')),
    re_path(r'^blog/', include('blog.urls')),
    re_path(r'^promotions/', include('promotions.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
