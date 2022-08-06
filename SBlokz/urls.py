from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from manufacturer import views as manu_views
from retailer import views as retail_views
urlpatterns = [
   path('', views.home, name='sb-home'),
   path('about/', views.about, name='sb-about'),
   path('blockchain/', views.blockchain, name='sb-blockchain'),
   path('connection/', views.connection, name='sb-connection'),
   path('logistics/', views.logistics, name='sb-logistics'),
   path('signup/', views.SignUpView.as_view(), name='sb-signup'),
   path('signup/retailer', retail_views.RetailerSignUpView.as_view(), name='retail-signup'),
   path('signup/manufacturer', manu_views.ManufacturerSignUpView.as_view(), name='manu-signup'),
]