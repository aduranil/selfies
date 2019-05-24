# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class Game(models.Model):
    room_name = models.CharField(max_length=50)
    users = models.ManyToManyField(User)
    game_status = models.CharField(max_length=50, default="active")

    def as_json(self):
        return dict(
            id=self.id,
            game_status=self.game_status,
            room_name=self.room_name)