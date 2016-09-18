from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^blog$', views.blogs),
    url(r'^comments/(?P<id>\d+)$', views.comments)
]
