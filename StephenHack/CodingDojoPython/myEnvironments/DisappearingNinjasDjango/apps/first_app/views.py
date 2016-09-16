from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, "first_app/index.html")

def ninjas(request):
	return render(request, "first_app/ninjas.html")

def show_ninja(request, color):

	if color == 'blue':
		request.session['link'] = 'leonardo.jpg'
	elif color == 'red':
		request.session['link'] = 'raphael.jpg'
	elif color == 'orange':
		request.session['link'] = 'michelangelo.jpg'
	elif color == 'purple':
		request.session['link'] = 'donatello.jpg'
	else:
		request.session['link'] = "notapril.jpg"

	return render(request, "first_app/ninja.html")



