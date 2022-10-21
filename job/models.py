from distutils import extension
from email.policy import default
from random import choices
from django.db import models
from django_countries.fields import CountryField
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.

def image_upload(instance , filename):   #function naming the imageuploded and folder 
    imagename , extension = filename.split(".")
    return "jobs/%s/%s.%s"%(instance.id,instance.id,extension)

class job(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE , related_name = 'job_owner')
     
    JOB_TYPES = (('Part Time' , 'Part Time') , ('full Time' , "Full Time"))
    title = models.CharField(max_length = 100)
    location = CountryField()
    job_type = models.CharField(choices = JOB_TYPES , max_length = 100)
    disccription = models.TextField(max_length = 1000 )
    published_at = models.DateTimeField(auto_now = True)
    vacancy = models.IntegerField(default = 1)
    salary = models.IntegerField(default = 0)
    experience_years = models.IntegerField(default = 0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload, height_field=None, width_field=None, max_length=100)
    slug = models.SlugField(max_length = 100 , blank = True , null = True)
    
    
    def save(self, *args , **kwargs) :
        if not self.slug:
            self.slug = slugify(self.title)
        super(job , self).save(*args , **kwargs) 
    
    
    
    def __str__(self):
        return self.title
     
class Category(models.Model):
    name = models.CharField(max_length = 25)
        
    def __str__(self):
        return self.name
        
    
class Apply(models.Model):
    job = models.ForeignKey(job, on_delete=models.CASCADE , related_name = 'apply_job')
    name = models.CharField(max_length = 150)
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length = 200)
    cv = models.FileField(upload_to='apply/')
    coverlitter = models.TextField(max_length = 500)
    created_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name
    
    
    
    
    