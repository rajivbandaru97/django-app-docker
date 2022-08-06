from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# Create your views here.
class SignUpView(TemplateView):
    template_name = 'sblokz/signup.html'
    
def home(request):
    if request.user.is_authenticated:
        if request.user.is_manufacturer:
            return redirect('manu-profile')
        elif request.user.is_retailer:
            return redirect('retail-profile2')
    return render(request, 'sblokz/index.html')

def about(request):
	return render(request, 'SBlokz/page1.html')

def blockchain(request):
	return render(request, 'SBlokz/blockchain.html')

def connection(request):
	return render(request, 'SBlokz/connection.html')

def logistics(request):
	return render(request, 'SBlokz/logistics.html')

def signup(request):
	return render(request, 'SBlokz/signup.html')

    

