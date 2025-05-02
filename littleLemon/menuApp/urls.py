from django.contrib import admin
from django.urls import path
from menuApp import views
urlpatterns = [
    path('',views.content,name='Content'),
    # path('drinks/<str:name>',views.drinks,name="Drinks"),
]