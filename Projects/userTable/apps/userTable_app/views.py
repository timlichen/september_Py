from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
    context = { "users": User.objects.all()}
    print context
    return render(request, "index.html", context)

def addUser(request):
    # calling an extended objects method.
    if User.objects.validatePresence(request.POST): # **
        User.objects.create(name=request.POST['name'], favorite_food=request.POST['favFood'], favorite_city=request.POST['favCity'])
    else:
        print "fail"

    return redirect("/")
