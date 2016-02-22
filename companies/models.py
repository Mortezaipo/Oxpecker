from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    site = models.URLField()
    logo = models.ImageField()
    introduction = models.TextField()
    user = models.ForeignKey(User)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
        

class Developer(models.Model):
    name = models.CharField(max_length=50)
    brief_introduction = models.CharField(max_length=150)
    company = models.ForeignKey(Company)
    picture = models.ImageField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
        
    def __unicode__(self):
        return "%s: %s" %(self.name, self.company.name)
