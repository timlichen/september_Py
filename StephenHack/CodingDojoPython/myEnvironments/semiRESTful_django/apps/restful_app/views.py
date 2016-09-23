from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def index(request):
	context = {
		'products' : Product.objects.all()
	}
	return render(request, 'restful_app/index.html', context)

def show(request, id):
	product = {
		'product' : Product.objects.get(id=id)
	}
	return render(request, 'restful_app/show.html', product)

def new(request):

	return render(request, 'restful_app/new.html')

def create(request):
	Product.objects.create(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
	return redirect('/products')

def edit(request, id):
	context =  {
		'product': Product.objects.get(id=id) 
	}
	return render(request, 'restful_app/edit.html', context)

def update(request, id):
	old_product = Product.objects.get(id=id)
	old_product.name = request.POST['name']
	old_product.description = request.POST['description']
	old_product.price = request.POST['price']
	old_product.save()
	return redirect('/products')

def remove(request, id):
	Product.objects.get(id=id).delete()
	return redirect('/products')
