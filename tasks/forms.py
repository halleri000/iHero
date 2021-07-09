from django import forms
from .models import Task
from user_app.models import HeroUser

class AddTaskForm(forms.ModelForm):
  class Meta: 
    model = Task
    fields = ['task']

class addTaskFormCoach(forms.Form):
  task = forms.CharField(max_length=400)
  assigned_to = forms.ModelChoiceField(queryset=HeroUser.objects.all())

# https://stackoverflow.com/questions/8466768/using-request-user-with-django-modelform 
