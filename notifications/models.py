from django.db import models
from django.utils import timezone
from user_app.models import HeroUser

# Create your models here.


class Message(models.Model):
    text = models.TextField()
    time_date = models.DateTimeField(default=timezone.now)
    assigned_message = models.ForeignKey(
        HeroUser,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True,
        related_name='assigned_message',
    )


class Notification(models.Model):
    mention = models.ForeignKey(
        Message,
        on_delete=models.CASCADE
    )
    mentioned_user = models.ForeignKey(
        HeroUser,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.mention
