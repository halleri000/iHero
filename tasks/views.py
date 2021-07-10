from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from .forms import AddTaskForm, addTaskFormCoach
from .models import Task

def newTaskByLearner(request):
  if request.method =="POST":
    form = AddTaskForm(request.POST)
    if form.is_valid():
      newTask = form.save(commit=False)
      newTask.assigned_to = request.user
      newTask.save()
      HttpResponse("Success")
  form = AddTaskForm()
  return render(request, 'generic_form.html', {'form': form})


def newTaskByCoach(request):
  if request.method=="POST":
    form = addTaskFormCoach(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      Task.objects.create(
        task = data['task'],
        assigned_to = data['assigned_to']
      )
      HttpResponse("Success")
  form = addTaskFormCoach()
  return render(request, "generic_form.html", {'form': form})

def taskDetailView(request, task_id):
  task = Task.objects.get(id=task_id)
  return render(request, 'task.html', {'task': task})


def markTaskComplete(request, task_id):
  task = Task.objects.get(id=task_id)
  task.completed = True
  task.save()
  if request.META:
        base = request.META['HTTP_REFERER']
        url = f'{base}'
        return HttpResponseRedirect(url)

def markTaskIncomplete(request, task_id):
  task = Task.objects.get(id=task_id)
  task.completed = False
  task.save()
  if request.META:
        base = request.META['HTTP_REFERER']
        url = f'{base}'
        return HttpResponseRedirect(url)
