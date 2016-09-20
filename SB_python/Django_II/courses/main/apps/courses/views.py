from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
	context = {
		"courses" : Course.objects.all()
	}
	return render(request, 'courses/index.html', context)

def add(request):
	Course.objects.create(name = request.POST['name'], description = request.POST['description'])
	return redirect('/')

def commence(request, id):
	context = {
		"course" : Course.objects.get(id=id)
	}
	return render(request, 'courses/destroy.html', context)

def complete(request, id):
	Course.objects.get(id=id).delete()
	return redirect('/')