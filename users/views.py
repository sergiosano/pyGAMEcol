from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from . import forms


def user_login(request):
    if request.user.is_authenticated:
        return redirect('collection')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('collection')
        else:
            messages.error(request, "Usuario y/o contraseña incorrectos.")

    return render(request, 'users/login.html')

def user_logout(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.user.is_authenticated:
        return redirect('collection')

    form = forms.RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = form.save()

        if user:
            login(request, user)
            return redirect('collection')

    return render(request, 'users/register.html', {'form': form})