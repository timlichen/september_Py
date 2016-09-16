from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
	if 'counter' in request.session:
		pass
	else:
		request.session['counter'] = 0
	if 'giant_string' in request.session:
		pass
	else:
		request.session['giant_string'] = ""
	return render(request, "first_app/index.html")

def process_gold(request):
	if request.POST['building'] == 'farm':
		temp = random.randrange(10,21)
		request.session['counter'] += temp
		request.session['giant_string'] += "You gained " + str(temp) + " gold"
	elif request.POST['building'] == 'cave':
		temp = random.randrange(5,11)
		request.session['counter'] += temp
		request.session['giant_string'] += "You gained " + str(temp) + " gold"
	elif request.POST['building'] == 'house':
		temp = random.randrange(2,6)
		request.session['counter'] += temp
		request.session['giant_string'] += "You gained " + str(temp) + " gold"
	elif request.POST['building'] == 'casino':
		temp = random.randrange(0,51)
		if random.randrange(0, 2) == 0:
			request.session['giant_string'] += "You gained " + str(temp) + " gold"
			request.session['counter'] -= temp
		else:
			request.session['giant_string'] += "You lost " + str(temp) + " gold"
			request.session['counter'] += temp
	return redirect('/')
	def reset(request):
		del request.session['giant_string']
		del request.session['counter']
	return redirect('/')


