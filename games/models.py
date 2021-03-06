from __future__ import unicode_literals
from django.db import models
from companies.models import Company
from licenses.models import License


def upload_logo(instance, filename):
    return "games/{}/logo.png".format(instance.name)


def upload_image(instance, filename):
    return "games/{}/intro.png".format(instance.name)

def upload_screenshot(instance, filename):
    return "games/{}/screenshots/{}".format(instance.game.name, instance.image)

def upload_package(instance, filename):
    return "games/{}/packages/{}.tar.gz".format(instance.game.name, instance.version)


class Game(models.Model):
    name = models.CharField(max_length=200, unique=True)
    introduction = models.TextField()
    company = models.ForeignKey(Company)
    license = models.ForeignKey(License)
    logo = models.ImageField(upload_to=upload_logo)
    image = models.ImageField(upload_to=upload_image)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Version(models.Model):
    change = models.TextField()
    version = models.CharField(max_length=10)
    package = models.FileField(upload_to=upload_package, default=None)
    game = models.ForeignKey(Game)
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.version

    class Meta:
        unique_together = (('version', 'game'),)


class Screenshot(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_screenshot)
    game = models.ForeignKey(Game)
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
