from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from ..login_reg_app.models import User 
from .models import Book

def index(request):
	context = {
		'user' : User.objects.all(),
		'books' : Book.objects.all()
	}
	return render(request, 'login_reg_app/index.html', context)

def home(request):

	return render(request, 'belt_app/home.html')

def add(request):

	return render(request, 'belt_app/add.html')

def create(request):
	Book.objects.create(title=request.POST['title'], author=request.POST['author_list'], review=request.POST['review'], rating=request.POST['rating'])

	return redirect('/create')
