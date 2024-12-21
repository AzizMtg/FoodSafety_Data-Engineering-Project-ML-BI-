from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Helper functions to check the user role
def is_inspector(user):
    return user.groups.filter(name='Inspector').exists()

def is_owner(user):
    return user.groups.filter(name='Owner').exists()

def is_client(user):
    return user.groups.filter(name='Client').exists()

@login_required
def dashboard_redirect(request):
    if is_owner(request.user):
        return redirect('profileOwner') 
    elif is_inspector(request.user):
        return redirect('profileInspector') 
    elif is_client(request.user):
        return redirect('profileClient')  # Redirect to profileClient page for Client
    else:
        return HttpResponseForbidden("You are not authorized to view this page")

# Profile views
@login_required
def profileInspector(request):
    return render(request, 'accounts/profileInspector.html')

@login_required
def profileClient(request):
    return render(request, 'accounts/profileClient.html')

@login_required
def profileOwner(request):
    return render(request, 'accounts/profileOwner.html')

# Login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('dashboard')  # Redirect to the dashboard after successful login
            else:
                messages.error(request, "Invalid credentials")
        else:
            messages.error(request, "Invalid form submission")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# Logout view
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('index')
