from django.urls import path
from tasks.views import add_task
urlpatterns = [
    path('add_task',add_task)
]
 