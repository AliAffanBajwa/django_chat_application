from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.views import redirect_to_login

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'authApp/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
        return render(request, 'authApp/register.html', {'form': form})

class LoginUserView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'authApp/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful!')
                return redirect('home')
            messages.error(request, 'Invalid credentials')
        else:
            messages.error(request, 'Invalid username or password')
        return render(request, 'authApp/login.html', {'form': form})

class LogoutUserView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'Logout successful!')
        return redirect('login')

