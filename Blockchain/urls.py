"""Blockchain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from SBlokz import views
from manufacturer import views as manu_views
from manufacturer.views import (
    OrderListView, 
    OrderDetailView,
    OrderCreateView,
    OrderUpdateView,
    OrderDeleteView,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    search,
)
from retailer import views as retail_views
from retailer.views import (
    OrderListView2, 
    OrderDetailView2,
    OrderCreateView2,
    OrderUpdateView2,
    OrderDeleteView2,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SBlokz.urls')),
    path('register/', manu_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='manufacturer/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='manufacturer/logout.html'), name='logout'),
    path('profile/', manu_views.profile, name='manu-profile'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', manu_views.change_friends, name='change_friends'),
    path('editprofile/', manu_views.editprofile, name='manu-editprofile'),
    path('order/', OrderListView.as_view(), name='manu-order'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='manu-detail'),
    path('order/new/', OrderCreateView.as_view(), name='manu-create'),
    path('order/<int:pk>/update/', OrderUpdateView.as_view(), name='manu-update'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='manu-delete'),
    path('product/', ProductListView.as_view(), name='manu-product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='manu-detail_product'),
    path('product/new/', ProductCreateView.as_view(), name='manu-create_product'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='manu-update_product'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='manu-delete_product'),
    path('search/', manu_views.search, name='verify'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='manufacturer/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='manufacturer/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='manufacturer/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='manufacturer/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    
    
     path('register2/', retail_views.register, name='register2'),
    path('profile2/', retail_views.profile, name='retail-profile2'),
    path('editprofile2/', retail_views.editprofile, name='retail-editprofile2'),
    path('order2/', OrderListView2.as_view(), name='retail-order2'),
    path('order2/<int:pk>/', OrderDetailView2.as_view(), name='retail-detail2'),
    path('order2/new/', OrderCreateView2.as_view(), name='retail-create2'),
    path('order2/<int:pk>/update/', OrderUpdateView2.as_view(), name='retail-update2'),
    path('order2/<int:pk>/delete/', OrderDeleteView2.as_view(), name='retail-delete2'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)