from django.urls import path
from tasks.views import user_dashboard,manager_dashboard,test,add_task,show_task
urlpatterns = [
    path('user-dashboard/',user_dashboard,name="userDashboard"),
    path('manager-dashboard/',manager_dashboard,name="ManagerDashboard"),
    path('test/',test),
    path('add/',add_task,name="createTask"),
    path('task/',show_task)
]
 