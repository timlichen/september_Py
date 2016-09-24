from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import AppUser
from ..login_reg_app.models import User

# Create your views here.
def index(request):
	return render(request, 'belt_app/home.html')

def add(request):

	return render(request, 'belt_app/add.html')

def create(request):
	
	AppUser.objects.create(email=request.session['email'], reviews=AppUser.objects.get(id=request.POST['review']), rating=AppUser.objects.get(id=request.POST['rating']))

	return redirect(reverse('belt_app:add'))