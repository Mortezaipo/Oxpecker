from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


def upload_company_logo(instance, filename):
    return "uploads/companies/{}/logo.png".format(instance.name) #FIXME: lower()

def upload_profile_picture(instance, filename):
    return "uploads/companies/{}/developers/{}.png".format(instance.company.name, instance.name) #FIXME: lower()


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    site = models.URLField()
    logo = models.ImageField(upload_to=upload_company_logo)
    introduction = models.TextField()
    user = models.ForeignKey(User)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
        

class Developer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    brief_introduction = models.CharField(max_length=150)
    company = models.ForeignKey(Company)
    picture = models.ImageField(upload_to=upload_profile_picture)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
        
    def __unicode__(self):
        return "%s: %s" %(self.name, self.company.name)
