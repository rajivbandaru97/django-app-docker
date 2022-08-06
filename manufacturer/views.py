from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import  login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import (
	ListView, 
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)
from .models import Profile
from SBlokz.models import User, Order, Product, Friend
from retailer.models import Profile2
from .forms import ManufacturerSignupForm, ManufacturerUpdateForm, ProfileUpdateForm, SearchForm


def search(request):
    template = 'SBlokz/product_detail.html'

    query = request.GET.get('q')

    if query:
    	results = Product.objects.filter(Q(hash_id__icontains=query) | Q(title__icontains=query))
    else:
    	results = Product.objects.all()

    return render(request, template, {'results': results})

class ManufacturerSignUpView(CreateView):
	model = User
	form_class = ManufacturerSignupForm
	template_name = 'manufacturer/register.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'manufacturer'
		return super().get_context_data(**kwargs)

	def get(request):
		users = User.objects.exclude(id=request.user.id)
		friend = Friend.objects.get(current_user=request.user)
		friends = friend.users.all()

		args = { 'users': users, 'friends': friends }
		return render(request, self.template_name, args)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('manu-profile')

	def change_friends(request, operation, pk):
		friend = User.objects.get(pk=pk)
		if operation == 'add':
			Friend.make_friend(request.user, friend)
		elif operation == 'remove':
			Friend.lose_friend(request.user, friend)
		return redirect('manufacturer/profile.html')



def register(request):
	if request.method == 'POST':
		form = ManufacturerSignupForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!You can now login to it')
			return redirect('login')
	else:
		 form = ManufacturerSignupForm()
	return render(request, 'manufacturer/register.html', {'form': form})

#CRUD
# create, update, retrieve, delete

def profile(request):
	context = {
		'orders': Order.objects.all(),
		'products': Product.objects.all() 
	}
	return render(request, 'manufacturer/profile.html', context)

def orders(request):
	context = {
		'orders': Order.objects.all()
	}
	return render(request, 'manufacturer/order.html', context)

def products(request):
		context = {
			'products': Product.objects.all()
		}
		return render(request, 'manufacturer/product.html')

def change_friends(request, operation, pk):
	friend = User.objects.get(pk=pk)
	if operation == 'add':
		Friend.make_friend(request.user, friend)
	elif operation == 'remove':
		Friend.lose_friend(request.user, friend)
	return redirect('manufacturer/profile.html')

class LoggedInMixin(object):

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class OrderListView(LoggedInMixin, ListView):
	model = Order
	template_name = 'manufacturer/order.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'orders'
	ordering = ['-date_ordered']

	def get_queryset(self):
		return Order.objects.filter(author=self.request.user)

class OrderDetailView(DetailView):
	model = Order

class OrderCreateView(LoginRequiredMixin, CreateView):
	model = Order
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class OrderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Order
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		order = self.get_object()
		if self.request.user == order.author:
			return True
		return False

class OrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Order
	success_url = '/order/'

	def test_func(self):
		order = self.get_object()
		if self.request.user == order.author:
			return True
		return False
		

class ProductListView(LoggedInMixin, ListView):
	model = Product
	template_name = 'manufacturer/product.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'products'

	def get_queryset(self):
		return Product.objects.filter(author=self.request.user)



class ProductDetailView(DetailView):
	model = Product

class ProductCreateView(LoginRequiredMixin, CreateView):
	model = Product
	fields = ['title', 'producttype', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Product
	fields = ['title', 'producttype', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		product = self.get_object()
		if self.request.user == product.author:
			return True
		return False

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Product
	success_url = '/product/'

	def test_func(self):
		product = self.get_object()
		if self.request.user == product.author:
			return True
		return False


def editprofile(request):
	if request.method == 'POST':
		u_form = ManufacturerUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, 
								   request.FILES, 
								   instance=request.user.profile)

		if u_form.is_valid and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Profile Updated!')
			return redirect('manu-profile')
	else:
		u_form = ManufacturerUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
	 'u_form': u_form,
	 'p_form': p_form
			  }

	return render(request, 'manufacturer/editprofile.html', context)