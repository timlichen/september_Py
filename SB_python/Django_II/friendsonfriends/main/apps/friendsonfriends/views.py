from django.shortcuts import render, redirect
from .models import User, Combo

# Create your views here.
def index(request):
	context = {
		'combos' : Combo.objects.all(),
		'choices' : User.objects.all()
	}
	return render(request, 'friendsonfriends/index.html', context)

def add(request):
	User.objects.create(username = request.POST['name'])
	return redirect('/')

def merge(request):
	first = User.objects.get(id = request.POST['choice1'])
	print first['username']
	second = User.objects.get(id = request.POST['choice2'])
	print second
	Combo.objects.create(first = first, second = second)
	return redirect('/')