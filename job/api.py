from cgitb import lookup
from pyexpat import model
from job.views import job_details
from rest_framework.response import Response
from .models import job
from .Serializer import JobSerializer
from rest_framework.decorators import api_view



@api_view(['GET'])
def job_list_api(request):
    all_jobs = job.objects.all()
    data = JobSerializer(all_jobs , many = True).data
    context = {"job_list": data}
    return Response(context)


@api_view(['GET'])
def job_detail_api(request , id):
    job_details = job.objects.get(id=id)
    data = JobSerializer(job_details ).data
    context = {"job_detail": data}
    return Response(context)


from rest_framework import generics

class JobListApi(generics.ListCreateAPIView):
    queryset = job.objects.all()
    serializer_class = JobSerializer
    
class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'

