"""pizza_delivery_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from .views import admin_login_view,admin_home_page_view,authenticate_admin,logout_admin,add_todo,home_page_view,user_registration,user_login_view,authenticate_user,user_home_page_view

urlpatterns = [
	path('',home_page_view,name = 'homepage'),
	path('user_registration/',user_registration),
	path('user/',user_login_view,name = 'user-loginpage'),
	path('authenticate_user/',authenticate_user),
	path('user/homepage/',user_home_page_view, name = 'user-homepage'),
    path('admin/',admin_login_view,name = 'admin-loginpage'),
    path('authenticate_admin/',authenticate_admin),
    path('admin/homepage/',admin_home_page_view, name = 'admin-homepage'),
    path('logout_admin/',logout_admin),
    path('add_todo/',add_todo)
]
