from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', views.admin, name='admin'),


    path('', views.home, name=''),
    path('home/', views.home, name='home'),
]
