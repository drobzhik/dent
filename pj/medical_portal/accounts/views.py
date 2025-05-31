from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('main_menu')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'accounts/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        user_type = request.POST.get('user_type')
        
        if password != password2:
            messages.error(request, "Passwords don't match")
        elif CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
        else:
            user = CustomUser.objects.create_user(
                username=username,
                password=password,
                user_type=user_type
            )
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
    
    return render(request, 'accounts/register.html')

@login_required
def main_menu_view(request):
    return render(request, 'accounts/main_menu.html')

def logout_view(request):
    logout(request)
    return redirect('login')