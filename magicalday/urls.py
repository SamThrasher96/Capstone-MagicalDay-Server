"""
URL configuration for magicalday project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls import include
from rest_framework import routers
from magicaldayapi.views import (register_user, login_user, GuestView, 
LocationView, MenuItemView, ReservationView, RestaurantDetailsView, 
RideDetailsView, ShowDetailsView, StaffShiftView, StaffView )

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'guests', GuestView, 'guest')
router.register(r'locations', LocationView, 'location')
router.register(r'menuitems', MenuItemView, 'menuitem')
router.register(r'reservations', ReservationView, 'reservation')
router.register(r'restaurantdetails', RestaurantDetailsView, 'restaurantdetail')
router.register(r'ridedetails', RideDetailsView, 'ridedetail')
router.register(r'showdetails', ShowDetailsView, 'showdetail')
router.register(r'staffshifts', StaffShiftView, 'staffshift')
router.register(r'staff', StaffView, 'staff')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
