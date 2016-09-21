from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
   url(r'^$', views.index, name = 'my_index'),
   url(r'^merge$', views.merge, name='integration_merge')
]