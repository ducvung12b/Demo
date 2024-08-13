from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('home/', views.home,name='home'),

     path('', views.viewhome,name='viewhome'),

     path('cart/',views.cart,name='cart'),

     path('detail/',views.detail,name='detail'),

     path('checkout/',views.checkout,name='checkout'), 

     path('update_item/',views.updateItem,name='update_item'), 

     path('login/',views.loginPage,name='login'), 

     path('logout/',views.logoutPage,name='logout'), 

     path('register/',views.register,name='register'), 

     path('search/',views.search,name='search'), 

     path('laptop/',views.laptop,name='laptop'), 
     
     path('pc/',views.pc,name='pc'), 

     path('phone/',views.phone,name='phone'), 

     path('edit/',views.edit,name='edit'), 
     
     # VIEW
     path('viewsearch/',views.viewsearch,name='viewsearch'), 

     path('viewlaptop/',views.viewlaptop,name='viewlaptop'), 
     
     path('viewpc/',views.viewpc,name='viewpc'), 

     path('viewphone/',views.viewphone,name='viewphone'), 

    

]
