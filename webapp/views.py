from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    context = {'home':home}
    return render(request, 'web/home.html', context)

@login_required(login_url='users:login')
def dashboard(request):
    context = {'dashboard':dashboard}
    return render(request, 'web/dashboard.html', context)