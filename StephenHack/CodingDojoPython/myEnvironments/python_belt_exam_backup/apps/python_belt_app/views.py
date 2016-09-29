from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.db.models import Count
from ..login_reg_app.models import User

def index(request):
	return render(request, 'python_belt_app/index.html')

