from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^destroy/(?P<id>\d+)$', views.commence),
    url(r'^destroy/complete/(?P<id>\d+)$', views.complete)
]