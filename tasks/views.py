from django.shortcuts import render,redirect
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskDetailsForm
from django.http import JsonResponse
from tasks.models import Employee,Task,TaskDetail,Project
from django.db.models import Q,Max,Min,Avg,Count
from datetime import date
from django.contrib import messages

# Create your views here.
def manager_dashboard(request):
    # Base Queri
    BASE_QUERY = Task.objects.select_related('details').prefetch_related('details__assigned_to').order_by('id')

    type = request.GET.get('type','all')

    # Counting for dashbord
    count = Task.objects.aggregate(
        total = Count('id'),
        completed_task = Count('id',filter=Q(status='COMPLETED')),
        task_InProgress = Count('id',filter=Q(status='IN_PROGRESS')),
        incomplete_task = Count('id',filter=Q(status='PENDING'))
        )
    
    # rendar task depend on cliking total/completed/in progress/or todos
    if type == "completed":
        tasks = BASE_QUERY.filter(status="COMPLETED")
    elif type == "InProgress":
        tasks = BASE_QUERY.filter(status="IN_PROGRESS")
    elif type == "incomplete":
        tasks = BASE_QUERY.filter(status="PENDING")
    else:
        tasks = BASE_QUERY

    context = {
        'tasks':tasks,
        'count':count
    }

    return render(request,'dashboard/manegar-dashbord.html',context)


def user_dashboard(request):
    return render(request,'dashboard/user-dashbord.html')

def add_task(request):
    # employee = Employee.objects.all()
    form = TaskForm()
    form2 = TaskDetailsForm()
    context = {
        "TaskForms":form,
        "TaskDetailsForm":form2
    }
    if request.method == 'POST':
        form = TaskForm(request.POST)
        form2 = TaskDetailsForm(request.POST)
        if form.is_valid() and form2.is_valid():
            task = form.save()
            task_details = form2.save(commit=False)
            task_details.taskToDetails = task
            task_details.save()
            form2.save_m2m()
            messages.success(request,'Task Added Successfully!')
            return redirect('createTask')
       
    context = {
        "TaskForms":form,
        "TaskDetailsForm":form2,
        "opareston_Type":'Create'
    }
    return render(request,'task_form.html',context)

def update_task(request,id):
    task = Task.objects.get(id=id)

    form = TaskForm(instance = task)
    form2 = TaskDetailsForm(instance = task.details)
    context = {
        "TaskForms":form,
        "TaskDetailsForm":form2
    }
    if request.method == 'POST':
        form = TaskForm(request.POST,instance = task)
        form2 = TaskDetailsForm(request.POST,instance = task.details)
        if form.is_valid() and form2.is_valid():
            task = form.save()
            task_details = form2.save(commit=False)
            task_details.taskToDetails = task
            task_details.save()
            form2.save_m2m()
            messages.success(request,'Task Update Successfully!')
            return redirect('updateTask',id=task.id)
    context = {
        "TaskForms":form,
        "TaskDetailsForm":form2,
        "opareston_Type":'Update'
    }
    return render(request,'task_form.html',context)

def delete_task(request,id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request,f"Task ID:{id} id Deleted Successfully!")
        return redirect('ManagerDashboard')
    else:
        messages.error(request,f"Something wen't Wrong")
        return redirect('ManagerDashboard')
    
