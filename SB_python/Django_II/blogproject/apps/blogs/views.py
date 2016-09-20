from django.shortcuts import render, HttpResponse
from .models import User

def index(request):
  print(User.objects.all())

  User.objects.create(first_name="mike",last_name="mike",password="1234asdf")
  print(User.objects.all())

  u = User.objects.get(id=1)
  print(u.first_name)

  u.first_name = "Joey"
  u.save()
  j = User.objects.get(id=1)
  print(j.first_name)

  print(User.objects.get(first_name="mike"))

  users = User.objects.raw("SELECT * from my_app_name_user")

  for user in users:
    print user.first_name
    
  return HttpResponse("ok")from django.shortcuts import render