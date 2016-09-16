from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'disninja/index.html')

def ninjas(request):
	return render(request, 'disninja/ninjas.html')

def moreninjas(request, color):
	if color == 'blue':
		urlink = 'disninja/blue.html'
	elif color == 'orange':
		urlink = 'disninja/orange.html'
	elif color == 'red':
		urlink = 'disninja/red.html'
	elif color == 'purple':
		urlink = 'disninja/purple.html'
	else:
		urlink = 'disninja/other.html'
		
	return render(request, urlink)