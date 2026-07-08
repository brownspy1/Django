from django.urls import path
from tasks.views import user_dashboard,manegar_dashboard,test,add_task
urlpatterns = [
    path('user-dashbord/',user_dashboard),
    path('manegar-dashbord/',manegar_dashboard),
    path('test/',test),
    path('add/',add_task)
]
 