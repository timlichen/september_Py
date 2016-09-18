from django.shortcuts import render, redirect
# from .models import user
from .models import User
# Create your views here.
def index(request):
	context = {'users': User.objects.all()}
	return render(request, 'first_app/index.html', context)

def addUser(request):
	User.objects.create(name=request.POST['name'], description=request.POST['description'])

	return redirect('/')

def removeUser(request):
	context = {'user': }
	return render(request, 'first_app/removeUser.html')