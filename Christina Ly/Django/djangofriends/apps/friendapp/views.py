from django.shortcuts import render, redirect, HttpResponse
from . models import Users, Friendships

def index(request):
	users = Users.objects.get(id = 1)
	context = {'users': [users]}
	return render(request, "friendapp/index.html", context)
	##users must be wrapped in an array for the get function to work
def filterlast(request):
	users = Users.objects.filter(last_name = "Rodriguez")	
	context = {'users': users}
	return render(request, "friendapp/index.html", context)
def excludelast(request):
	users = Users.objects.exclude(last_name = "Rodriguez")
	context = {'users': users}
	return render(request, "friendapp/index.html", context)
def chaining(request):
	users = Users.objects.filter(last_name = "Rodriguez") | Users.objects.filter(first_name ="Daniel")
	context = {'users': users}
	return render(request, "friendapp/index.html", context) 
def madison(request):
	users = Users.objects.filter(last_name = "Rodriguez").exclude(first_name = "Madison")
	context = {'users': users} 
	return render(request, "friendapp/index.html", context)	
def danmike(request):
	users = Users.objects.exclude(first_name ="Daniel").exclude(first_name = "Michael")
	context = {'users': users}
	return render(request, "friendapp/index.html", context)
def getrodriguez(request):
	users = Users.objects.get(last_name = "Rodriguez")
	print users
	context = {'users': users}
	return render(request, "friendapp/index.html", context)
	#### errors will occur for get function if more than one result
def getthousand(request):
	users = Users.objects.get(id = 10000)
	context = {'users': users}
	return render(request, "friendapp/index.html", context)
	#### errors will occur because query matching does not exist