from dataclasses import fields
import imp
from django import forms
from .models import Apply , job
from job import models



class ApplyForm(forms.ModelForm):  #cause it have model in model
    class Meta:
        model = Apply
        fields = {'name' , 'email' ,'website' ,'cv' ,'coverlitter'}
        

class JobForm(forms.ModelForm):
    class Meta:
        model = job
        fields = '__all__'
        exclude = ('slug','owner')
        
