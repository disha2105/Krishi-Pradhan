from django.contrib import admin
from django.urls import path
from Krishi_Pradhan import views

urlpatterns = [
    path("", views.home, name='Krishi_Pradhan'),
    path("registration/", views.registration, name='registration'),
    path("login/", views.login, name='login'),
    path("home/", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("about2/", views.about2, name='about'),
    path("organic/", views.organic, name='organic'),
    path("organic2/", views.organic2, name='organic'),
    path("registration/home", views.home, name='about2'),
    path("login/questionnare/", views.questionnare, name='question'),
    path("questionnare/", views.questionnare, name='question'),
    path("home2/", views.home2, name='home2')
]
