from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    context = {'home':home}
    return render(request, 'web/home.html', context)


def dashboard(request):
    context = {'dashboard':dashboard}
    return render(request, 'web/dashboard.html', context)