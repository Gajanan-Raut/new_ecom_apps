from django.contrib import admin
from django.urls import path
from new_ecom_app import views
urlpatterns = [
    path('index', views.index),
]
