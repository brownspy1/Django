from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def sign_up(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()

    return render(request,'sign-up/sign-up.html',{'form':form})
