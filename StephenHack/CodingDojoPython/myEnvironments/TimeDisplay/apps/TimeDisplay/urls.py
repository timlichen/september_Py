from django.conf.urls import url
from . import views

def index(request):
	print ("bananapeel")

urlpatterns = [
   url(r'^$', views.index)
]
