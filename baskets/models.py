from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from games.models import Version


class Basket(models.Model):
    user = models.ForeignKey(User)
    game = models.ForeignKey(Version)
    created_datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s: %s" %(self.user.username, self.game.game.name)