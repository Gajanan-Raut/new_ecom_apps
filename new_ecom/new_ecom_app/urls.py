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
#     path('set',views.setcookie),
#     path('get',views.getcookie),
#     path('setsession',views.setsession),
#     path('getsession',views.getsession),
#     path('delsession',views.del_session),
#     path('getid',views.getloggeduserid),
    path('set', views.setcookie),
    path('get',views.getcookie),
    path('del',views.del_cookie),

    # SET SESSION
    path('setsession',views.setsession),
    path('getsession',views.getsession),
    path('del_session',views.del_session),
    path('getid',views.getloggeduserid),
]
