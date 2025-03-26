"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('index', views.index, name='index'),
    path('register',views.register,name='register'),
    path('',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('profile', views.profile ,name='profile'),
    path('update/<int:id>', views.update ,name='update'),
    path('main', views.main, name='main'),
    path('blog', views.blog, name='blog'),
    path('blogdetails', views.blogdetails, name='blogdetails'),
    path('checkout', views.checkout, name='checkout'),
    path('bill_detail', views.bill_detail, name="bill_detail"),
    path('contact', views.contact, name='contact'), 
    path('shopdetails', views.shopdetails, name='shopdetails'),
    path('productdetails/<int:id>', views.productdetails, name='productdetails'),
    path('wishlist_product/<int:id>', views.wishlist_product, name='wishlist_product'),
    path('shopgrid', views.shopgrid, name='shopgrid'),
    path('shopingcart', views.shopingcart, name='shopingcart'),
    path('addtocart/<int:id>', views.addtocart, name='addtocart'),
    path('clr_filter', views.clr_filter, name='clr_filter'),
    path('size_filter', views.size_filter, name='size_filter'),
    path('price_filter',views.price_filter, name='price_filter'),
    path('minuscart/<int:id>', views.minuscart , name="minuscart"),
    path('pluscart/<int:id>', views.pluscart, name="pluscart"),
    path('removecart/<int:id>', views.removecart , name="removecart"),
]
