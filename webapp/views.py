from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .form import *
from django.contrib import messages
from .models import Record
from django.db.models import Q
import logging


# Create your views here.


#Home
def home(request):
    context = {'home':home}
    return render(request, 'web/home.html', context)

#Dashboard
@login_required(login_url='users:login')
def dashboard(request):
    sort_param = request.GET.get('sort', '-id')
    records = Record.objects.all().order_by(sort_param)
    next_sort = 'id' if sort_param == '-id' else '-id'
    context = {'records':records,
               'next_sort': next_sort,
               'current_sort': sort_param,
               }
    return render(request, 'web/dashboard.html', context)

#Create
@login_required(login_url='users:login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Created Successfully!")
            return redirect('webapp:dashboard')   #urls name
    else:
        form = CreateRecordForm()
        
    context = {'form':form}
    
    return render(request, 'web/create-record.html', context=context)  #templates location



#Detail
@login_required(login_url='users:login')
def detail_record(request, slug):
    record = get_object_or_404(Record, slug=slug)  # to show me hhtp404 if ther's no objectin database
    if request.method == 'POST':
        form = CreateRecordForm(request.POST, instance=record)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.record = record
            myform.save()
            return redirect('webapp:dashboard')
    
    else:
        form = CreateRecordForm(instance=record)
        
    context = {'record': record, 'form': form}
    
    return render(request, 'web/detail-record.html', context)
    

#Edit
@login_required(login_url='users:login')
def edit_record(request, slug):
    record = get_object_or_404(Record, slug=slug)  # to show me hhtp404 if ther's no objectin database
    if request.method == 'POST':
        form = CreateRecordForm(request.POST, instance=record)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.record = record
            myform.save()
            messages.success(request, 'Record is Updated.')
            return redirect('webapp:detail-record', slug=record.slug)    
    else:
        form = CreateRecordForm(instance=record)
        
    context = {'record': record, 'form': form}
    
    return render(request, 'web/edit-record.html', context)

# Delete
@login_required(login_url='users:login')
def delete_record(request, slug):
    record = get_object_or_404(Record, slug=slug)
    if request.method == 'POST':
        record.delete()
        messages.warning(request, "Record Deleted Successfully!")
        return redirect('webapp:dashboard')
    
    context = {'record':record}
    
    return render(request, 'web/delete-record.html', context)


logger = logging.getLogger(__name__)
@login_required(login_url='users:login')
def search(request):
    query = request.GET.get('query', '').strip()
    results = []
    try:
        if query:
            results = Record.objects.filter(Q(first_name__icontains=query)|Q(last_name__icontains=query)|Q(phone__istartswith=query))
            
    except Exception as e:
        logger.error('Error during search: %s', e)
        
    context = {'results':results,
                   'query':query}
        
    return render(request, 'web/search.html', context=context)
        
    
    
def custom_page_not_found(requset, exception):
    return render(requset, 'web/404.html', status=404)