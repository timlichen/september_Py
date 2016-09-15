from django.shortcuts import render, HttpResponse
import random
def index(request):
	if not (request.session['counter']):
		request.session['counter'] = 0
	else:
		request.session['counter'] += 1
	return render(request, 'first_app/index.html')

def submit(request):
	words = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	request.session['random_word'] = ''.join(random.choice(words) for _ in range(14))
	return render(request, 'first_app/index.html')
