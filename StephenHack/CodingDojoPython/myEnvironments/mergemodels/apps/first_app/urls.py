from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='index'), 
    url(r'^addUser', views.addUser, name='addUser'),
    url(r'^(?P<id>\d+)/destroy$', views.destroy, name='destroy')
]