from django.contrib import admin
from django.urls import path
from new_ecom_app import views
urlpatterns = [
    path('index', views.index),
    path('indexs', views.forms),
    path('delete/<id>', views.delete),
    path('edit/<id>', views.edit),
    path('register/', views.register),
    path('header', views.header),
    path('login/', views.user_login),
    path('logout', views.user_logout),
]
