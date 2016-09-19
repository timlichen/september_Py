from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Email

# Create your views here.
def index(request):
	return render(request, 'emailvalid/index.html')

def process(request):
	try:
		validate_email(request.POST['email'])
	except ValidationError:
		context = {
			"invalid_alert" : "Invalid email"
		}
		return render(request, 'emailvalid/index.html', context)
	Email.objects.create(email = request.POST['email'])
	context = {
		"emails" : Email.objects.all(),
		"current" : request.POST['email']
	}
	return render(request, 'emailvalid/emails.html', context)