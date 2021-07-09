from django.shortcuts import render
from .forms import CreateHeroForm
from .models import HeroUser
from tasks.models import Task






# more to do here, just created the view to match the form/model, error catching needs to be worked on as well
def createUser(request):
  if request.method == 'POST':
    form = CreateHeroForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      if HeroUser.objects.filter(username=data['username']).exists()==False:
        if data['password1'] == data['password2']:
          user = HeroUser.objects.create_user(
          username=data['username'],
          first_name=data['first_name'],
          last_name=data['last_name'],
          email=data['email'],
          password=data['password1'],
          interests = data['interests'], 
          website = data['website'],
          bio = data['bio'],
          age=data['age']
        )
        if data['is_coach'] == True:
          user.is_staff = True
          user.save()
        
        return render(request, '????????.html', {'form': form})
  form = CreateHeroForm()
  return render(request, '?????????.html', {'form': form})


def learner_details(request, user_id: int):
    learner = HeroUser.objects.get(id=user_id)
    assigned_tasks = Task.objects.filter(assigned_to=learner)
    context = {
        'learner': learner,
        'assigned_tasks': assigned_tasks,
    }
    return render(request, 'learner_details.html', context)


def heroes(request):
    heroes = HeroUser.objects.all()
    context = {
        'heroes': heroes
    }
    return render(request, 'heroes.html', context)
