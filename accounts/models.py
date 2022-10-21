from distutils import extension
from email.policy import default
from random import choices
from django.db import models
from django.forms import CharField
from django_countries.fields import CountryField
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User , max_length = 100 , on_delete=models.CASCADE)
    city = models.ForeignKey('City' , related_name = 'user_city' , on_delete=models.CASCADE , blank = True , null = True)
    phone_number = models.CharField( max_length = 15)
    image = models.ImageField(upload_to='accounts/user', height_field=None, width_field=None, max_length=100)
    join_data = models.DateTimeField(auto_now = True)
    location = CountryField()
    slug = models.SlugField(blank = True , null = True)

    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user)
        return super(Profile, self).save(*args, **kwargs)
    
    def __str__(self):
        return '%s'%(self.user)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        

class City (models.Model):
    name = models.CharField( max_length = 15)
    
    def __str__ (self):
        return self.name