from django.contrib import admin
from notifications.models import Notification, Message

# Register your models here.
admin.site.register(Notification)
admin.site.register(Message)
