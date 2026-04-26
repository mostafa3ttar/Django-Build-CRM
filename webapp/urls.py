from django.urls import path
from . import views

app_name = ''

urlpatterns = [
    path('', views.index),
    path('register/', views.register, name='register'),
]
