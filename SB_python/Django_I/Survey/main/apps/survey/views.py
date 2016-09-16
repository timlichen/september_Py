from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'survey/index.html')

def process(request):
	if 'count' in request.session:
		request.session['count'] += 1
	else:
		request.session['count'] = 1
	request.session['data'] = [request.POST['name'], request.POST['location'], request.POST['lang'], request.POST['comm']]
	return redirect('/result')

def result(request):
	return render(request, 'survey/result.html')

def back(request):
	return redirect('/')