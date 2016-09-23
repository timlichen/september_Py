from django.shortcuts import render, redirect
from .models import Course
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
	context = {'users': Course.objects.all()}
	return render(request, 'first_app/index.html', context)

def addUser(request):
	Course.objects.create(name=request.POST['name'], description=request.POST['description'])

	return redirect(reverse('courses:index'))

def destroy(request, id):
	course_to_delete = Course.objects.get(id=id)
	if request.method == "GET":
		return render(request, 'courses_app/confirm_delete.html', { 'course' : course_to_delete })
	else:
		course_to_delete.delete()
    	return redirect(reverse('courses:index'))