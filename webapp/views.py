from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .form import *


# Create your views here.

def home(request):
    context = {'home':home}
    return render(request, 'web/home.html', context)

@login_required(login_url='users:login')
def dashboard(request):
    context = {'dashboard':dashboard}
    return render(request, 'web/dashboard.html', context)

@login_required(login_url='users:login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webapp:dashboard')
    else:
        form = CreateRecordForm()
        
    context = {'form':form}
    
    return render(request, 'web/create-record.html', context=context) 
    
    