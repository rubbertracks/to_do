from django.shortcuts import render
from .models import Task
from django.shortcuts import redirect
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView


class Tasklistview(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task1'


class TaskDetailview(DetailView):
    model = Task
    template_name = 'details.html'
    ontext_object_name = 'task'


class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    ontext_object_name = 'task'
    fields = ['name', 'priority', 'date']


def index(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
    return render(request, 'index.html', {'task': task1})


# def details(request):

#     return render(request,'details.html',{'task':task})

def base(request):
    return render(request, 'base.html')


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'update.html', {'f': f, 'task': task})

# def get_success_url(self):
#     return reverse_lazy('details',kwargs={'pk':self.object.id})