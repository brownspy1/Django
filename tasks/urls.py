from django.urls import path
from tasks.views import user_dashboard,manager_dashboard,add_task,update_task,delete_task
urlpatterns = [
    path('user-dashboard/',user_dashboard,name="userDashboard"),
    path('manager-dashboard/',manager_dashboard,name="ManagerDashboard"),
    path('add/',add_task,name="createTask"),
    path('update/<int:id>/',update_task,name='updateTask'),
    path('delete/<int:id>/',delete_task,name="deleteTask")
]
 