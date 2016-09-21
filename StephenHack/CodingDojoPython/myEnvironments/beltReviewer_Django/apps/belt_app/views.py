from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
	return render(request, 'login_reg_app/index.html')

def home(request):
	return render(request, '')
