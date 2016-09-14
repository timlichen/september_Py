from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'VMVC/index.html')
def show(request):
	print request.method
	return render(request, 'VMVC/show_users.html')
def create(request):
	print request.method
	if request.method == "POST":
		request.session['name'] = request.POST['first_name']
		return render(request, 'VMVC/show_users.html')
	else:
		return redirect('/')