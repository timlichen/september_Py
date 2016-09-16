#first app

from django.conf.urls import url
from . import views
import re

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas$', views.ninjas),
    url(r'^ninjas/(?P<color>[a-zA-Z]+)$', views.show_ninja)
]