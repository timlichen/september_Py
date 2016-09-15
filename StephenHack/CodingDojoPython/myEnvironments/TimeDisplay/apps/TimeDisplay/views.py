import datetime

from django.shortcuts import render, HttpResponse
def index(request):
   	context = {
   	"Time": datetime.datetime.now()
   	} 
	return render(request,'TimeDisplay/page.html', context)