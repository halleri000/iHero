from django.db import models
from django.contrib.auth.models import AbstractUser

class HeroUser(AbstractUser):
  SERVICEINDUSTRY= "SI"
  TECH ='TK'
  SALES = 'SL'
  HEALTHCARE = 'HC'
  FINANCE = 'FN'
  EDUCATION = 'ED'

  INTEREST_CHOICES = [
    (SERVICEINDUSTRY, 'Service Industry'),
    (TECH, 'Technology'),
    (SALES, 'Sales'),
    (HEALTHCARE, 'Health Care'), 
    (FINANCE, 'Finance'),
    (EDUCATION, 'Education')
  ]



  email= models.EmailField(max_length=254)
  age = models.IntegerField(default=18)
  interests = models.CharField(choices = INTEREST_CHOICES, max_length=2, default=TECH)
  bio = models.TextField()
  website = models.URLField(max_length=200)
  is_coach = models.BooleanField(default=False)
  
  def __str__(self):
    return self.username


