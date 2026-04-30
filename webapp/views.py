from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .form import *
from django.contrib import messages
from .models import Record


# Create your views here.

def home(request):
    context = {'home':home}
    return render(request, 'web/home.html', context)

@login_required(login_url='users:login')
def dashboard(request):
    record = Record.objects.all()
    context = {'record':record}
    return render(request, 'web/dashboard.html', context)

@login_required(login_url='users:login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Post Created Successfully!")
            return redirect('webapp:dashboard')
    else:
        form = CreateRecordForm()
        
    context = {'form':form}
    
    return render(request, 'web/create-record.html', context=context) 
    
    