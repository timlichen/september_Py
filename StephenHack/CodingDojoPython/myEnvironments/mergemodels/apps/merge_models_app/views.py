from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.db.models import Count
from ..first_app.models import Course
from ..login_reg_app.models import User
from .models import Merge

# Create your views here.
def index(request):
	numbers = Merge.objects.values('course').annotate(num_users=Count('user')).distinct().order_by('course_id')
	context = {
		'courses': Course.objects.all(),
		'users': User.objects.all(),
		'number_users' : numbers
	}

	return render(request, 'merge_models_app/index.html', context)

def merge(request):
	Merge.objects.create(course=Course.objects.get(id=request.POST['course']), user = User.objects.get(id=request.POST['user']))

	return redirect('/')