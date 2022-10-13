from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('job_list/', views.job_list , name = 'job_list'),
    path('job_details/', views.job_details , name = 'job_details'),
]