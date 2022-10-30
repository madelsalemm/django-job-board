from django.contrib import admin
from django.urls import path , include
from . import views
from .api import job_list_api , job_detail_api , JobListApi , JobDetail
from job import api

app_name = "jobs"

urlpatterns = [
    path('', views.job_list , name = 'job_list'),
    path('add', views.add_job , name = 'add_job'),
    
    ######## Start API ##################
    path('api/jobs', api.job_list_api , name = 'job_api'),
    path('api/jobs/<int:id>', api.job_detail_api , name = 'job_detail_api'),
    ######## Class based View ##########
    path('api/v2/jobs/', api.JobListApi.as_view() , name = 'jobListapi'),
    path('api/v2/jobs/<int:id>', api.JobDetail.as_view() , name = 'job_detail_api_v2'),
    ######## end API ##################
    path('<str:slug>', views.job_details , name = 'job_details'),
]