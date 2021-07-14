from django import forms
from django.forms.widgets import PasswordInput, Textarea, URLInput

class CreateHeroForm(forms.Form):
  SERVICEINDUSTRY= "Service Industry"
  TECH ='Technology'
  SALES = 'Sales'
  HEALTHCARE = 'Health Care'
  FINANCE = 'Finance'
  EDUCATION = 'Education'
  INTEREST_CHOICES = [
    (SERVICEINDUSTRY, 'Service Industry'),
    (TECH, 'Technology'),
    (SALES, 'Sales'),
    (HEALTHCARE, 'Health Care'), 
    (FINANCE, 'Finance'),
    (EDUCATION, 'Education')
  ]
  COACH_CHOICES =[
    (True, 'Coach'),
    (False, 'Learner')]
  username = forms.CharField(max_length=150)
  first_name = forms.CharField(max_length=150)
  last_name = forms.CharField(max_length=150)
  interests = forms.CharField(widget = forms.Select(choices=INTEREST_CHOICES))
  email = forms.EmailField()
  password1 = forms.CharField(widget=PasswordInput)
  password2 = forms.CharField(widget=PasswordInput)
  website = forms.CharField(widget = URLInput)
  bio = forms.CharField(widget= Textarea)
  age = forms.IntegerField()
  is_coach = forms.CharField(widget=forms.Select(choices=COACH_CHOICES))



class LoginHeroForm(forms.Form):
  username = forms.CharField(max_length=150)
  password = forms.CharField(widget = PasswordInput)