from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from authapp import views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
]
