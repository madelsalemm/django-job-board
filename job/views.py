from multiprocessing import context
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .models import job , Apply
from django.core.paginator import Paginator
from .form import ApplyForm , JobForm
# Create your views here.

def job_list(request):
    job_list = job.objects.all()
    paginator = Paginator(job_list, 4) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'all_jobs' : page_obj}   #{'name in html' : name of all data above}
    return render (request , 'job/job_list.html' ,context)

def job_details(request , slug):
    job_details = job.objects.get(slug=slug)
    
    if request.method == 'POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_details
            myform.save()
    else:
        form = ApplyForm()         
    context = {'job_det' : job_details , 'form' : form}
    return render (request , 'job/job_detail.html' , context)

def add_job (request):
    if request.method == 'POST':
        form = JobForm(request.POST , request.FILES)
        if form.is_valid:
            myform = form.save(commit=False)    #stop save while i edite
            myform.owner = request.user         #to know who apply the form
            myform.save()
            return redirect('jobs:job_list')
    else:
        form = JobForm()
    context = {'form':form}
    return render (request , 'job/add_job.html' , context)
