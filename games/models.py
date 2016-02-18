from __future__ import unicode_literals
from django.db import models
from companies.models import Company
from licenses.models import License


class Game(models.Model):
    name = models.CharField(max_length=200, unique=True)
    introduction = models.TextField()
    company = models.ForeignKey(Company)
    license = models.ForeignKey(License)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Version(models.Model):
    changes = models.TextField()
    version = models.IntegerField()
    game = models.ForeignKey(Game)
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.version


class ScreenShot(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    game = models.ForeignKey(Game)
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
