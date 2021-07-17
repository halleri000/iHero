from django.shortcuts import render, HttpResponseRedirect
from .forms import AddTaskForm, addTaskFormCoach
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def newTaskByLearner(request):
  if request.method =="POST":
    form = AddTaskForm(request.POST)
    if form.is_valid():
      newTask = form.save(commit=False)
      newTask.assigned_to = request.user
      newTask.save()
      form = AddTaskForm()
      return render(request, 'generic_form.html', {'form': form, 'title': "New Task", 'message': "Would you like to add something else to your list?"})
  form = AddTaskForm()
  return render(request, 'generic_form.html', {'form': form, 'title': "New Task", 'message': "Please add a new task to your list!"})

@login_required
def newTaskByCoach(request):
  if request.method=="POST":
    form = addTaskFormCoach(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      Task.objects.create(
        task = data['task'],
        assigned_to = data['assigned_to']
      )
      form = addTaskFormCoach()
      return render(request, 'generic_form.html', {'form': form, 'title': "New Task", 'message': "Would you like to add something else to your or someone else's list?"})
  form = addTaskFormCoach()
  return render(request, "generic_form.html", {'form': form, 'title': "New Task", "message": "Please add a new task to either your list or someone else's"})


@login_required
def taskDetailView(request, task_id):
  task = Task.objects.get(id=task_id)
  return render(request, 'task.html', {'task': task})


@login_required
def markTaskComplete(request, task_id):
  task = Task.objects.get(id=task_id)
  task.completed = True
  task.save()
  if request.META:
        base = request.META['HTTP_REFERER']
        url = f'{base}'
        return HttpResponseRedirect(url)
  else:
    return HttpResponseRedirect(f'/task/{task_id}')


@login_required
def markTaskIncomplete(request, task_id):
  task = Task.objects.get(id=task_id)
  task.completed = False
  task.save()
  if request.META:
        base = request.META['HTTP_REFERER']
        url = f'{base}'
        return HttpResponseRedirect(url)
  else:
    return HttpResponseRedirect(f'/task/{task_id}')
