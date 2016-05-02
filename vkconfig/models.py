from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Playlist(models.Model):

    id = models.AutoField('#', primary_key = True)
    user = models.ForeignKey(User)
    playlist_name = models.CharField(max_length = 100)
    total_duration = models.IntegerField()
    num_songs = models.IntegerField()
