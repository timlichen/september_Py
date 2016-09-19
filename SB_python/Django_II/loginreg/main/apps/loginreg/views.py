from django.shortcuts import render, redirect
from .models import User
import bcrypt

# Create your views here.
def index(request):
	return render(request, 'loginreg/index.html')

def login(request):
	email = request.POST['email']
	password = email, request.POST['password']
	user = User.objects.login(email, password)
	if len(request.session['errors']) > 0:
		return render(request, 'loginreg/index.html')
	else:
		return render(request, 'loginreg/success.html', user)

def register(request):
	firstName = request.POST['first_name']
	lastName = request.POST['last_name']
	email = request.POST['email']
	password = request.POST['password']
	dblCheck = request.POST['dblcheck']
	errors = User.objects.register(firstName, lastName, email, password, dblCheck)
	if len(errors) > 0:
		return render(request, 'loginreg/index.html', errors)
	else:
		password = password.encode()
		print password
		realPass = bcrypt.hashpw(password, bcrypt.gensalt())
		User.objects.create(first_name = firstName, last_name = lastName, email = email, password = realPass)
		context = {
			'user' : User.objects.get(first_name = firstName)
		}
		print context['user']['name']
		return render(request, 'loginreg/success.html', context)

def logoff(request):
	return redirect('/')