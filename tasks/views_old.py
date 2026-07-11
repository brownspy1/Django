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
    BASE_QUERY = Task.objects.select_related('details').prefetch_related('details__assigned_to')

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
    elif type == "all":
        tasks = BASE_QUERY.all()

    context = {
        'tasks':tasks,
        'count':count
    }

    return render(request,'dashboard/manegar-dashbord.html',context)

def user_dashboard(request):
    return render(request,'dashboard/user-dashbord.html')

def test(request):
    context = {
        "names" :["mahadi","mahir"]
    }
    return render(request,'test.html',context)

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
           
            # This data for Django form
            # {'title': 'Demo task', 'description': 'this is tasks', 'due_date': datetime.date(2026, 8, 17), 'assigned_to': ['1']}
            # task = form.cleaned_data
            # title = task.get('title')
            # description = task.get('description')
            # due_date = task.get('due_date')
            # assigned_to = task.get('assigned_to')
            # # assign task on db
            # task_one = Task.objects.create(title=title, description=description, due_date=due_date)
            # # assign task details
            # task_one_details = TaskDetail.objects.create(taskToDetails=task_one)
            # # assign all employees to task
            # for emp_id in assigned_to:
            #     # get employee by id
            #     emp_object = Employee.objects.get(id=emp_id)
            #     task_one_details.assigned_to.add(emp_object)
            # This data for Django model form

            # return JsonResponse({"status": "success", "message": "Task added successfully!"}, status=201)
    context = {
        "TaskForms":form,
        "TaskDetailsForm":form2
    }
    return render(request,'task_form.html',context)
def update_task(request):
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
        "TaskDetailsForm":form2
    }
    return render(request,'task_form.html',context)

def show_task(request):
    # task = Task.objects.all()
    # task_filtar = Task.objects.filter(is_completed=True)
    # task = TaskDetail.objects.exclude(priority="L")
    # task = Task.objects.filter(title__icontains='b')
    '''filtar out with titel contain c and status pending '''
    # tasks = Task.objects.filter(title__icontains='c', status='PENDING')

    '''filtar out with titel contain x or status pending '''
    # tasks = Task.objects.filter(Q(title__icontains='X') | Q(status='PENDING'))


    # task = Task.objects.all()
    # task = Employee.objects.all()

    ''' Optimaizd quary for revars relason'''
    # task = Task.objects.select_related('project').all()

    ''' try fiinding undar project haw many task in this project'''
    # projects = Project.objects.prefetch_related('tasks').all()
    ''' try fiinding undar task haw many employy in this project'''
    # tasks = Task.objects.prefetch_related('details__assigned_to').all()

    '''-------------try to use aggrita from sql to django orm --------------'''

    # tasks = Task.objects.aggregate(num_task=Count('id'))
    ''' learning anotaison on aggriigason woth order by'''
    # tasks = Task.objects.annotate(employye_count = Count('details__assigned_to')).order_by('employye_count') #ordar by desanding

    # tasks = Task.objects.filter(due_date='2026-07-11')
    tasks = Task.objects.select_related('details').exclude(details__priority='L').all()
    return render(request,'tasks.html',{'tasks':tasks})