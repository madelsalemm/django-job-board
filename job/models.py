from email.policy import default
from random import choices
from django.db import models

# Create your models here.

class job(models.Model):
    JOB_TYPES = (('part' , 'Part Time') , ('full' , "Full Time"))
    
    title = models.CharField(max_length = 100)
    job_type = models.CharField(choices = JOB_TYPES , max_length = 100)
    disccription = models.TextField(max_length = 1000 )
    published_at = models.DateTimeField(auto_now = True)
    vacancy = models.IntegerField(default = 1)
    salary = models.IntegerField(default = 0)
    experience_years = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.title
     
    
    