from django.db import models

from user_app.models import HeroUser
from django.utils import timezone


class Task(models.Model):
  task = models.CharField(max_length=400)
  assigned_to = models.ForeignKey(HeroUser, on_delete=models.CASCADE)
  submitted_on = models.DateTimeField(default = timezone.now)
  completed = models.BooleanField(default=False)

  def __str__(self):
    return self.task