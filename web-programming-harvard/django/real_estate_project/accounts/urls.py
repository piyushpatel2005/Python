from django.urls import path

from . import views

urlpatterns = [
    # empty means it will be used for /listings
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]
