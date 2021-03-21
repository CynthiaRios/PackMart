"""PackMart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
import shops.views
#from . import views

urlpatterns = [
    url(r'^shops/$',                    TemplateView.as_view(template_name='welcome.html'), name='welcome'),
    url(r'^register/',                  shops.views.register, name='register'),
    url(r'^shop/$',                     shops.views.shop_list,                   name='shop_list'),
    url(r'^shop/$',                     shops.views.my_shop_list,                   name='my_shop_list'),
    url(r'^shop/(?P<id>[0-9]+)/$',      shops.views.shop_read,                   name='shop_read'),
    url(r'^shop/update/(?P<id>[0-9]+)/$',      shops.views.shop_update,                 name='shop_update'),
    url(r'^shop/new/$',                 shops.views.shop_create,                 name='shop_create'),
    url(r'^product/(?P<id>[0-9]+)/$',      shops.views.product_read,                   name='product_read'),
    url(r'^shops/',                     include('shops.urls')),
    url(r'^$',                          TemplateView.as_view(template_name='welcome.html'), name='welcome'),
    url(r'^admin/',                     admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
