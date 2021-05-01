from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.generic import ListView, DetailView
from django.http import Http404
from .models import Product
from .forms import BookNurseForm
from .utils import Util 
# from cart.models import Cart
# Create your views here.


from cart.forms import CartAddProductForm
def intro_page(request):
	return render(request, "preghome/list.html",{})

def aboutus(request):
	return render(request, "preghome/aboutus.html",{})

def nurse_package(request):
	form = BookNurseForm(request.POST or None)
	context = {
		"form":form,
	}
	return render(request, "preghome/nurse.html",context)

def product_list(request):
	queryset = Product.objects.all()
	return render(request, "preghome/products.html", {"qs":queryset})

def our_team(request):
	return render(request, "preghome/team.html", {})

def our_partners(request):
	return render(request, "preghome/partners.html", {})	

def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	related_prods = Product.objects.all()
	cart_product_form	=	CartAddProductForm()
	return render(request, 'preghome/detail.html',{'object':product,'cart_product_form':cart_product_form,'related':related_prods})

#====writing a view to book anurse
def booknurse(request):
	form = BookNurseForm(request.POST or None)
	if form.is_valid():
		contact = form.cleaned_data.get("contact")
		location = form.cleaned_data.get("location")
		no_days = form.cleaned_data.get("no_days")
		package = forms.cleaned_data.get("package")

		order_data = (contact,location,no_days,package)

		receiver_mail = 'preghealth0@gmail.com'#email to act as recipient
		email_body='Hi team please client is requesting for this bed side package,\n'+str(order_data)
		test_data = {'email_body':email_body,'to_email':receiver_mail,'email_subject':'PregHealth Order details'}
		
		Util.send_email(test_data)
		return redirect('preghome:nurse_success')		
	else:
		return redirect('preghome:booknurse')


def book_success(request):
	return render(request, 'preghome/nurse_success.html',{})