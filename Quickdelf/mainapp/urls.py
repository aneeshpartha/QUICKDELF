from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

app_name = "mainapp"

urlpatterns = [

    url(r'index/$', views.Hotelview.as_view() , name='index'),  # Mainpage URL
    url(r'register/' , views.UserProfileview.as_view() , name='register'), # Registration page URL
    url(r'login/$' , views.loginview.as_view() , name='login'), # Login page URL
    url(r'items/(?P<hotel_id>[0-9]+)/$' , views.itemsview , name='items'), #Items URL
    url(r'items/(?P<items_hotel_id>[0-9]+)/(?P<items_id>[0-9]+)/$' , views.itemscartcalc , name='cart_list'), # Items selected in a particular restaurant
    url(r'items/cart/$' , views.cartview.as_view() , name='cart'), # Cart URL
    url(r'items/payment/$' , views.paymentview.as_view() , name='payment'), # Payment URL

]


