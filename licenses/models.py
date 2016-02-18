from __future__ import unicode_literals
from django.db import models


class License(models.Model):
    name = models.CharField(max_length=50, unique=True)
    body = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
