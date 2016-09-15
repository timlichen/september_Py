from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'survey/index.html')

def result(request):
	if 'count' in request.session:
		request.session['count'] += 1
	else:
		request.session['count'] = 1
	return render(request, 'survey/result.html')

def back(request):
	return redirect('/')