from django.contrib import admin
from django.urls import path
from Src import views
urlpatterns = [
    path('', views.index, name='Home'),
]
