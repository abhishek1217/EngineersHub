from django.contrib import admin
from django.urls import path
from QES import views

urlpatterns = [
    path('',views.index,name="Landing"),
]