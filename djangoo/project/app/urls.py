from django.urls import path
from . import views

app_name = 'app';

urlpatterns = [
    path('download_link/', views.download_link , name='downloadLink'),
]