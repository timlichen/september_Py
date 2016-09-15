from django.shortcuts import render, redirect
import random
import string

def index(request):
	request.session['grow'] = 0
	return render(request, 'ranwords/index.html')
def new(request):
	request.session['grow'] += 1
	request.session['gen'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(14))
	return render(request, 'ranwords/index.html')