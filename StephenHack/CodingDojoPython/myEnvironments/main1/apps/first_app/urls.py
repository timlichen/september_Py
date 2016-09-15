#  From inside apps/first_app/urls.py
  from django.conf.urls import url
  from . import views           # This line is new!

  urlpatterns = [
    url(r'^$', views.index)     # This line has changed!
  ]