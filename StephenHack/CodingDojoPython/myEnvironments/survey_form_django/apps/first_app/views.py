from django.shortcuts import render, HttpResponse, redirect

def index(request):

	if 'counter' in request.session:
		pass
	else:
		request.session['counter'] = 0

	return render(request, 'first_app/index.html')

def survey(request):
	request.session['counter'] += 1

	info = {
	'Name': request.POST['Name'],
	'Location': request.POST['dojoLoc'],
	'Language': request.POST['favLang'],
	'comments': request.POST['comments']
	}
	request.session['info'] = info
	return redirect('/result')

def result(request):
	return render(request, 'first_app/result.html')




# 	return render(request, 'first_app/result.html')