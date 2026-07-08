from django.db import models


class Task(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE, default=1, related_name="tasks")
    title = models.CharField(max_length=250)
    description = models.TextField()
    due_date = models.DateField()
    STATUS_OPTIONS = (
        ('PENDING','Pending'),
        ('IN_PROGRESS','In Progress'),
        ('COMPLETED','Completed')
    )
    status = models.CharField(max_length=16,choices=STATUS_OPTIONS,default='PENDING')
    is_completed = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class TaskDetail(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_OPTIONS = (
        (HIGH,'High'),
        (MEDIUM,'Medium'),
        (LOW,'Low')
        )
    taskToDetails = models.OneToOneField(Task,on_delete=models.CASCADE, related_name="details")
    assigned_to = models.ManyToManyField("Employee",related_name="tasks")
    priority = models.CharField(max_length=2,choices=PRIORITY_OPTIONS,default=LOW)
    notes = models.TextField(null=True,blank=True)


class Project(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True,null=True)
    start_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=254)

    def __str__(self):
        return f'{self.name} (ID : {self.id})'