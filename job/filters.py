import django_filters
from .models import job

class JobFilter(django_filters.FilterSet):
    disccription = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = job
        fields = ['location', 'category' , 'experience_years', 'job_type' , 'disccription' , 'title']