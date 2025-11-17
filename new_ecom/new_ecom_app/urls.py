from django.contrib import admin
from django.urls import path
from new_ecom_app import views
urlpatterns = [
    path('index', views.index),
    path('indexs', views.forms),
    path('delete/<id>', views.delete),
    path('edit/<id>', views.edit),
]
