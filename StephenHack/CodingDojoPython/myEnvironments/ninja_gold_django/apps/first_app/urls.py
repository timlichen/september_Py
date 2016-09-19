#first app
from django.conf.urls import url
from . import views
import re

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_gold', views.process_gold),
    url(r'^sessionClear', views.sessionClear)
]