from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^products$', views.index, name = "my_products"),
    url(r'^products/create$', views.create, name = "my_create"),
    url(r'^products/process$', views.process, name = "my_process"),
    url(r'^products/(?P<id>\d+)/destroy$', views.destroy, name = "my_destroy"),

]