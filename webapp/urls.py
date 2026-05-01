from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'webapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-record/', views.create_record, name='create-record'),
    path('detail/<slug:slug>/', views.detail_record, name='detail-record'),
    path('edit/<slug:slug>/', views.edit_record, name='edit-record'),
    path('delete/<slug:slug>/', views.delete_record, name='delete-record'),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)