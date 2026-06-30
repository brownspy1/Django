from django.urls import path
from tasks.views import user_dashboard,manegar_dashboard
urlpatterns = [
    path('user-dashbord/',user_dashboard),
    path('manegar-dashbord/',manegar_dashboard)
]
 