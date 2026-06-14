from django.shortcuts import render, redirect
from django.db.models import Q
from tasks.models import *

# Create your views here.

def home_page(request):
    data = TaskModel.objects.all()
    status = request.GET.get('status')
    if status:
        data = TaskModel.objects.filter(status = status)
    context = {
        'data' : data,
        'status': status
    }
    return render(request, 'home.html', context)

def view_task(request, t_id):
    data = TaskModel.objects.get(id = t_id)
    context = {
        'data' : data
    }
    return render(request, 'task-view.html', context)

def task_list(request):
    data = TaskModel.objects.all()
    search = request.GET.get('search')
    if search:
        data = TaskModel.objects.filter(
            Q(title__icontains = search) |
            Q(priority__icontains = search) |
            Q(status__icontains = search)
        )
    context = {
        'data' : data,
        'search' : search
    }
    return render(request, 'task-list.html', context)

def task_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')
        task_image = request.FILES.get('task_image')
        
        TaskModel.objects.create(
            title = title,
            description = description,
            priority = priority,
            status = status,
            due_date = due_date,
            task_image = task_image
        )
        return redirect('task_list')
    return render(request, 'add-task.html')

def edit_task(request, t_id):
    data = TaskModel.objects.get(id = t_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        status = request.POST.get('status')
        due_date = request.POST.get('due_date')
        task_image = request.FILES.get('task_image')
        
        data.title = title
        data.description = description
        data.priority = priority
        data.status = status
        data.due_date = due_date
        if task_image:
            data.task_image = task_image
        data.save()
        return redirect('task_list')
    context = {
        'data' : data
    }
    return render(request, 'edit-task.html', context)

def delete_task(request, t_id):
    TaskModel.objects.get(id = t_id).delete()
    return redirect('task_list')
