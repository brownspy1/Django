from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm,TaskForm,TaskDetailsForm
from django.http import JsonResponse
from tasks.models import Employee,Task,TaskDetail
# Create your views here.

def user_dashboard(request):
    return render(request,'dashboard/user-dashbord.html')
def manegar_dashboard(request):
    return render(request,'dashboard/manegar-dashbord.html')

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
            
            return render(request,'task_form.html',{"TaskForms":form,"TaskDetailsForm":form2,'message':'Data added on database!'})
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