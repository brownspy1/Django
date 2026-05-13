from django.urls import path
from tasks.views import add_task,show_spacific_task
urlpatterns = [
    path('add_task',add_task),
    path('show_spacific_task/<id>/',show_spacific_task)
]
 