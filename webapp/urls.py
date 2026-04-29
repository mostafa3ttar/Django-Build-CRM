from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-record/', views.create_record, name='create-record'),
]
