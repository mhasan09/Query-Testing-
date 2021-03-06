"""QuerySetTesting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from queryApp.views import *

urlpatterns = [
    path('', data_send, name="home"),
    path('data', data_load, name="data"),
    path('chart', chart, name="data"),
    path('data/<int:id>/', detail_view_via_form, name="customers"),
    path('dataq/<int:id>/', detail_view, name="customersq"),
    path('customer_saved', updateUser.as_view(), name="customer_saved"),
    path('map', map, name="customers"),
]
