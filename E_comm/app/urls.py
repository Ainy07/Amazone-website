from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import *
from . models import *


urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>/',
         views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='show_cart'),
    path('pluscart/', views.plus_cart, name="pluscart"),
    path('minuscart/', views.minus_cart, name="minuscart"),
    path('removecart/', views.remove_cart, name="removecart"),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('login/', views.login, name='login'),

    path('checkout/', views.checkout, name='checkout'),
    path('emptycart/', views.emptycart),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('laptop/', views.laptop, name='laptop'),
    path('laptop/<slug:data>', views.laptop, name='laptopdata'),
    path('topwear/', views.topwear, name='topwear'),
    path('topwear/<slug:data>', views.topwear, name='topweardata'),
    path('bottomwear/', views.bottomwear, name='bottomwear'),
    path('bottomwear/<slug:data>', views.bottomwear, name='bottomweardata'),
    path('registration/', views.CustomerRegistrationView.as_view(),
         name='customerregistration'),
    path('account/login/', auth_views.LoginView.as_view(template_name='app/login.html',
         authentication_form=LoginForm), name='login'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
