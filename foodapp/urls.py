from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns=[
    path('index/',views.index,name='index'),
    path('add_item/',views.add_fooditem,name='addfooditem'),
    path('update_item/',views.update,name='updatefooditem'),
    ]

