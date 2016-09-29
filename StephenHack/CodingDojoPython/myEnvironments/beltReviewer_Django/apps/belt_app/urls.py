from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.index, name = 'login'), #login
   url(r'^books$', views.home, name='home'), #home
   url(r'^add$', views.add, name='add'),
   url(r'^create$', views.create, name='create')
  # url(r'^)
]