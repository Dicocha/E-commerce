from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

# import logging

# Create your views here.
def log_out(request):
    logout(request)
    return redirect('products:home')

def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html', {
            'form': UserCreationForm
        })
    
    elif request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            # Move this block of code to querys class
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return render(request, 'products/home.html')

            except:
                return render(request, 'users/register.html', {
                    'form': UserCreationForm,
                    'error': "User already exist"
                })
        else:
            return render(request, 'users/register.html', {
                'form': UserCreationForm,
                'error': "Password do not match"
            })