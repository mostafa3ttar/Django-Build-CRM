from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import CustomUserCreationForm, LoginForm
from django.contrib import messages

# Create your views here.


def register(request):
    # form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration is successfully')
            return redirect('users:login')
    else:
        form = CustomUserCreationForm()
    
    context = {'form':form}      
    
    return render(request, 'users/register.html', context)


# login user

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST) 
        if form.is_valid:
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            # authentication
            user = authenticate(request, username=username,password=password)
            
            if user is not None:
                login(request, user)
                # messages.success(request, 'Login is successfully')
                return redirect('webapp:dashboard')
    
    else:
        form = LoginForm()
        
    context = {'form': form}
    
    return render(request, 'users/login.html', context)

def my_logout(request):
    logout(request)
    # messages.success(request, 'Logout is Done!')
    return redirect('users:login')
