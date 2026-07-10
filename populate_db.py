import os
import django
import random
from faker import Faker

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskManegment.settings')
django.setup()

from tasks.models import Employee, Project, Task, TaskDetail

def populate_db():
    # Initialize Faker
    fake = Faker()

    # 1. Create Projects
    projects = []
    for _ in range(5):
        project = Project.objects.create(
            name=fake.bs().capitalize(),
            description=fake.paragraph()
            # start_at দেওয়া লাগবে না, কারণ মডেলে auto_now_add=True আছে
        )
        projects.append(project)
    print(f"Created {len(projects)} projects.")

    # 2. Create Employees
    employees = []
    for _ in range(10):
        employee = Employee.objects.create(
            name=fake.name(),
            email=fake.email()
        )
        employees.append(employee)
    print(f"Created {len(employees)} employees.")

    # 3. Create Tasks and TaskDetails
    for _ in range(20):
        # টাস্ক তৈরি
        task = Task.objects.create(
            project=random.choice(projects),
            title=fake.sentence(),
            description=fake.paragraph(),
            due_date=fake.date_this_year(),
            status=random.choice(['PENDING', 'IN_PROGRESS', 'COMPLETED']),
            is_completed=random.choice([True, False])
        )
        
        # টাস্কের ডিটেইলস তৈরি (মডেল অনুযায়ী ওয়ান-টু-ওয়ান ফিল্ডের নাম taskToDetails)
        task_detail = TaskDetail.objects.create(
            taskToDetails=task,
            priority=random.choice(['H', 'M', 'L']),
            notes=fake.paragraph()
        )
        
        # মেনি-টু-মেনি (ManyToMany) রিলেশনে এমপ্লয়ি যুক্ত করা
        # random.sample দিয়ে ১ থেকে ৩ জন এমপ্লয়ি সিলেক্ট করা হচ্ছে
        sampled_employees = random.sample(employees, random.randint(1, 3))
        task_detail.assigned_to.set(sampled_employees)

    print("Created 20 tasks and their corresponding details successfully.")
    print("Database populated successfully!")

if __name__ == "__main__":
    populate_db()