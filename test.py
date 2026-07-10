from tasks.models import Task,TaskDetail,Project,Employee
from datetime import date,timedelta
from django.db.models import Q,Count

# 1. Show the tasks which are assigned to a specific employee
def hw_1():
    emps = Employee.objects.prefetch_related('tasks__taskToDetails').get(id=4)
    print(emps.name)
    for task in emps.tasks.all():
        print(f' {task.taskToDetails.title}')

# 2. Show all employees working on a specific project

def hw_2():
    project = Project.objects.prefetch_related('tasks__details__assigned_to').get(id=2)
    print(project.name)
    i = 1
    for task in project.tasks.all():
        for employee in task.details.assigned_to.all():
            print(f' {i}.{employee.name}')
            i=i+1

# 3. Get all tasks that are due today
def hw_3():
    tasks = Task.objects.filter(due_date='2026-07-11').all()
    print('Hello')
    for task in tasks:
        print(f'Title: {task.title}\nDue Date: {task.due_date}')

# 4. Show all tasks with a priority higher than 'low'
def hw_4():
    tasks = Task.objects.select_related('details').exclude(details__priority='L').all()
    for task in tasks:
        print(f'Task: {task.title}\nPriority: {task.details.priority}')

# 5. Get the number of tasks completed by a specific employee
def hw_5():
    employee = Employee.objects.annotate(task = Count('tasks__taskToDetails',filter=Q(tasks__taskToDetails__status='COMPLETED'))).get(id=1)

    print(f'Name: {employee.name}\nTasks: {employee.task}\nStatus:')

    for i in employee.tasks.select_related('taskToDetails').all():
        if i.taskToDetails.status == 'COMPLETED':
            print(i.taskToDetails.status)

# 6. Get the most recently assigned task

def hw_6():
    task = Task.objects.order_by('-created_at').first()
    print(task.title)

# Show all projects that have no tasks assigned
def hw_7():
    project = Project.objects.filter(tasks__isnull=True)
    for pro in project:
            print(pro.name)

# 8. Show tasks that have been overdue for more than a week
def hw_8():
    sevenDayAgo = date.today()-timedelta(days=7)
    tasks = Task.objects.filter(due_date__lt =sevenDayAgo)
    for task in tasks:
        print(task.title)


# 9. Get the total count of tasks assigned to each employee

def hw_9():
    employee = Employee.objects.annotate(task = Count('tasks'))
    for emp in employee:
        print(f'Employee: {emp.name}\nAssign Tasks:{emp.task}')

# 10. Get tasks that are either 'completed' or 'in-progress'

def hw_10():
    tasks = Task.objects.filter(Q(status='COMPLETED')|Q(status='IN_PROGRESS'))
    # tasks = Task.objects.filter(status__in=['COMPLETED','IN_PROGRESS']) #morden clen minimal
    for task in tasks:
        print(f'Task: {task.title}\nStatus: {task.status}')