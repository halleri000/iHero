from django.core.management.base import BaseCommand
from tasks.models import Task
from user_app.models import HeroUser

class Command(BaseCommand):
  def handle(self, *args, **options):
    HeroUser.objects.bulk_create([
      HeroUser(username='Staff1', first_name='First2', last_name='Last2', email="email1@e.com", password='password1', website="http://website1.com", bio="a bio about a user", age='34', interests="SI", is_coach=True, is_staff=True),
      HeroUser(username='Staff2', first_name='First2', last_name='Last2', email="email1@e.com", password='password1', website="http://website1.com", bio="a bio about a user", age='34', interests="SL", is_coach=True, is_staff=True),
      HeroUser(username='Staff3', first_name='First2', last_name='Last2', email="email1@e.com", password='password1', website="http://website1.com", bio="a bio about a user", age='34', interests="HC", is_coach=True, is_staff=True),
      HeroUser(username='Staff4', first_name='First2', last_name='Last2', email="email1@e.com", password='password1', website="http://website1.com", bio="a bio about a user", age='34', interests="TK", is_coach=True, is_staff=True),
      HeroUser(username='Staff5', first_name='First2', last_name='Last2', email="email1@e.com", password='password1', website="http://website1.com", bio="a bio about a user", age='34', interests="FN", is_coach=True, is_staff=True),
      HeroUser(username='Staff6', first_name='First2', last_name='Last2', email="email1@e.com", password='password1', website="http://website1.com", bio="a bio about a user", age='34', interests="ED", is_coach=True, is_staff=True),
      HeroUser(username='User1', first_name='First1', last_name='Last1', email="email1@e.com", password='password1', website="http://website1.com", bio="a bio about a user", age='34', interests="SI"),
      HeroUser(username='User2', first_name='First2', last_name='Last2', email="email1@e.com", password='password1', website="http://website1.com", bio="a bio about a user", age='34', interests="SI"),
      HeroUser(username='User3', first_name='First1', last_name='Last1', email="email1@e.com", password='password1', website="http://website1.com", bio="a bio about a user", age='34', interests="SL"),
      HeroUser(username='User4', first_name='First2', last_name='Last2', email="email1@e.com", password='password1', website="http://website1.com", bio="a bio about a user", age='34', interests="SL"),
      HeroUser(username='User5', first_name='First1', last_name='Last1', email="email1@e.com", password='password1', website="http://website1.com", bio="a bio about a user", age='34', interests="HC"),
      HeroUser(username='User6', first_name='First2', last_name='Last2', email="email1@e.com", password='password1', website="http://website1.com", bio="a bio about a user", age='34', interests="HC"),
      HeroUser(username='User7', first_name='First2', last_name='Last2', email="email1@e.com", password='password1', website="http://website1.com", bio="a bio about a user", age='34', interests="TK"),
      HeroUser(username='User8', first_name='First2', last_name='Last2', email="email1@e.com", password='password1', website="http://website1.com", bio="a bio about a user", age='34', interests="TK"),
      HeroUser(username='User9', first_name='First2', last_name='Last2', email="email1@e.com", password='password1', website="http://website1.com", bio="a bio about a user", age='34', interests="FN"),
      HeroUser(username='User10', first_name='First2', last_name='Last2', email="email1@e.com", password='password1', website="http://website1.com", bio="a bio about a user", age='34', interests="FN"),
      HeroUser(username='User11', first_name='First2', last_name='Last2', email="email1@e.com", password='password1', website="http://website1.com", bio="a bio about a user", age='34', interests="ED"),
    ])

    Task.objects.bulk_create([
      Task(task="Ask questions", assigned_to=HeroUser.objects.get(username='User1')),
      Task(task="Seek knowledge", assigned_to=HeroUser.objects.get(username='User1')),
      Task(task="Ask questions", assigned_to=HeroUser.objects.get(username='User2')),
      Task(task="Seek knowledge", assigned_to=HeroUser.objects.get(username='User2')),
      Task(task="Ask questions", assigned_to=HeroUser.objects.get(username='User3')),
      Task(task="Seek knowledge", assigned_to=HeroUser.objects.get(username='User3')),
      Task(task="Ask questions", assigned_to=HeroUser.objects.get(username='User4')),
      Task(task="Seek knowledge", assigned_to=HeroUser.objects.get(username='User4')),
      Task(task="Ask questions", assigned_to=HeroUser.objects.get(username='User5')),
      Task(task="Spread positivity", assigned_to=HeroUser.objects.get(username='User5')),
      Task(task="Ask questions", assigned_to=HeroUser.objects.get(username='User6')),
      Task(task="Spread positivity", assigned_to=HeroUser.objects.get(username='User6')),
      Task(task="Ask questions", assigned_to=HeroUser.objects.get(username='User7')),
      Task(task="Spread positivity", assigned_to=HeroUser.objects.get(username='User7')),
      Task(task="Ask questions", assigned_to=HeroUser.objects.get(username='User8')),
      Task(task="Spread positivity", assigned_to=HeroUser.objects.get(username='User8')),
      Task(task="Ask questions", assigned_to=HeroUser.objects.get(username='User9')),
      Task(task="Study new information", assigned_to=HeroUser.objects.get(username='User9')),
      Task(task="Ask questions", assigned_to=HeroUser.objects.get(username='User10')),
      Task(task="Study new information", assigned_to=HeroUser.objects.get(username='User10')),
      Task(task="Ask questions", assigned_to=HeroUser.objects.get(username='User11')),
      Task(task="Study new information", assigned_to=HeroUser.objects.get(username='User11')),
      Task(task="Ask questions", assigned_to=HeroUser.objects.get(username='User11')),
      Task(task="Ask questions", assigned_to=HeroUser.objects.get(username='User6')),

    ])