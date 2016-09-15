from django.shortcuts import render
import time

# Create your views here.
def index(request):
	context = {"somekey": time.asctime()}
	return render(request,'timedisplay/page.html', context)