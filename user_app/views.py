from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import CreateHeroForm, LoginHeroForm
from .models import HeroUser
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required





def loginUser(request):
  if request.method == "POST":
    form = LoginHeroForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      if HeroUser.objects.filter(username=data['username']).exists():
        user = authenticate(username=data['username'], password=data['password'])
        login(request, user)
        return HttpResponseRedirect(request.GET.get('next', reverse('?????')))
      else:
        return render(request, 'genericform.html', {'form': form, 'title': 'Login Page', 'message': 'If you already have an account, please verify that you are using correct login credentials. If you do not have an account, please create one'})
  form = LoginHeroForm()
  return render(request, 'genericform.html', {'form': form, 'title': "Login Page", 'message': 'Please Login into your account'})


def createUser(request):
  if request.method == 'POST':
    form = CreateHeroForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      if HeroUser.objects.filter(username=data['username']).exists()==False:
        if data['password1'] == data['password2']:
          new_user = HeroUser.objects.create_user(
          username=data['username'],
          first_name=data['first_name'],
          last_name=data['last_name'],
          email=data['email'],
          password=data['password1'],
          interests = data['interests'], 
          website = data['website'],
          bio = data['bio'],
          age=data['age'],
          is_coach = data['is_coach']
          )
          if data['is_coach'] == True:
            new_user.is_staff = True
            new_user.save()
          user = authenticate(username=data['username'], password=data['password1'])
          login(request, user)
          return HttpResponseRedirect(reverse('home'))
        else:
          return render(request, 'genericform.html', {'form': form, 'message': "Please make sure passwords match", 'title': "Create New Account"})
      else:
        return render(request, 'genericform.html', {'form': form, 'title': "Create New Account", 'message': 'Username is unavailable, please choose another.'})
  form = CreateHeroForm()
  return render(request, 'genericform.html', {'form': form, 'title': "Create New Account", 'message': "Please fill out this form to create your new account"})

def loginUser(request):
  if request.method == "POST":
    form = LoginHeroForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      if HeroUser.objects.filter(username=data['username']).exists():
        user = authenticate(username=data['username'], password=data['password'])
        login(request, user)
        return HttpResponseRedirect(request.GET.get('next', reverse('home')))
      else:
        return render(request, 'genericform.html', {'form': form, 'title': 'Login Page', 'message': 'If you already have an account, please verify that you are using correct login credentials. If you do not have an account, please create one'})
  form = LoginHeroForm()
  return render(request, 'genericform.html', {'form': form, 'title': "Login Page", 'message': 'Please Login into your account'})