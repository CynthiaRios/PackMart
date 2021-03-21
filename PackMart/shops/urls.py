from django.conf.urls import url
from . import views
from rest_framework.authtoken import views as rest_framework_views

app_name = 'shops'

urlpatterns = [
    url(r'^',                                          views.index,                       name='index'),
]
