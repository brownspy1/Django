from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Hello World!")
def add_task(request):
    return HttpResponse('Task added')
def show_spacific_task(request,id):
    return HttpResponse(f'this is id : {id}')

def dashbord(request):
    return HttpResponse("Dashbord")