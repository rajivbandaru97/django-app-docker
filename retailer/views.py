from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth.models import User
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
from SBlokz.models import User, Order, Product
from retailer.models import Profile2
from .forms import RetailerSignupForm, RetailerUpdateForm, Profile2UpdateForm

User = get_user_model()

def users_list():
	users = Profile2.objects.exclude(user=exclude.user)
	context = {
				'users': users
	}
	return render(request, "retailer/profile2.html", context)

class RetailerSignUpView(CreateView):
    model = User
    form_class = RetailerSignupForm
    template_name = 'retailer/register2.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'retailer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('retail-profile2')

def register(request):
	if request.method == 'POST':
		form = RetailerSignupForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!You can now login to it')
			return redirect('login')
	else:
		 form = RetailerSignupForm()
	return render(request, 'retailer/register2.html', {'form': form})



def profile(request):
	if request.method == 'POST':
		form = RetailerSignupForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}!You can now login to it')
			return redirect('login')
	else:
		 form = RetailerSignupForm()
	return render(request, 'retailer/profile2.html')

def profile(request):
	context = {
		'orders': Order.objects.all(),
		'products': Product.objects.all()
	}
	return render(request, 'retailer/profile2.html', context)

def orders(request):
	context = {
		'orders': Order.objects.all()
	}
	return render(request, 'retailer/order2.html', context)

class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class OrderListView2(LoggedInMixin, ListView):
	model = Order
	template_name = 'retailer/order2.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'orders'
	ordering = ['-date_ordered']

	def get_queryset(self):
		return Order.objects.filter(author=self.request.user)

class OrderDetailView2(DetailView):
    model = Order

class OrderCreateView2(LoginRequiredMixin, CreateView):
	model = Order
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class OrderUpdateView2(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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

class OrderDeleteView2(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Order
	success_url = '/order2/'

	def test_func(self):
		order = self.get_object()
		if self.request.user == order.author:
			return True
		return False
def editprofile(request):
	if request.method == 'POST':
		u_form = RetailerUpdateForm(request.POST, instance=request.user)
		p_form = Profile2UpdateForm(request.POST, 
								   request.FILES, 
								   instance=request.user.profile)

		if u_form.is_valid and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Profile Updated!')
			return redirect('retail-profile2')
	else:
		u_form = RetailerUpdateForm(instance=request.user)
		p_form = Profile2UpdateForm(instance=request.user.profile)

	context = {
	 'u_form': u_form,
	 'p_form': p_form
			  }

	return render(request, 'retailer/editprofile2.html', context)

def profile_view(request, slug):
	p = Profile2.objects.filter(slug=slug).first()
	u = p.user
	sent_friend_requests = FriendRequest2.objects.filter(from_user=p.user)
	rec_friend_requests = FriendRequest2.objects.filter(to_user=p.user)

	friends = p.friends.all()

	# is this user our friend
	button_status = 'none'
	if p not in request.user.profile.friends.all():
		button_status = 'not_friend'

		# if we have sent him a friend request
		if len(FriendRequest.objects.filter(
			from_user=request.user).filter(to_user=p.user)) == 1:
				button_status = 'friend_request_sent'

	context = {
		'u': u,
		'button_status': button_status,
		'friends_list': friends,
		'sent_friend_requests': sent_friend_requests,
		'rec_friend_requests': rec_friend_requests
	}

	return render(request, "retailer/profile2.html", context)