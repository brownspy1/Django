from django.urls import path
from .views import sign_up

urlpatterns = [
    path("Sign-Up/",sign_up,name="signup")
]
