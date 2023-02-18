from django.urls import path
from django.shortcuts import render,redirect
from .import views
from .views import postview,likepost

urlpatterns = [
path("", views.index),
path("home", views.home),

path("postview", views.postview),
path("likepost", views.likepost),


]
