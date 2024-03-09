"""
URL configuration for officeReservation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from officeRes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.Home.as_view(), name='main'),
    path('add_room/', views.Add_room.as_view(), name='add_room'),
    path('room/delete/<int:id>/', views.Delete_room.as_view(), name='delete_room'),
    path('room/modify/<int:id>/', views.Modify_room.as_view(), name='modify_room'),
    path('room/reserve/<int:id>/', views.Reverve_room.as_view(), name='reserve_room'),
    path('room/<int:id>/', views.Room_detail.as_view(), name='reserve_room'),
]
