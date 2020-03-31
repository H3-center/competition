from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Target_list,Job
from .form import *
from django.shortcuts import get_object_or_404

# Create your views here.
def main(request):
    return HttpResponse("This is Jobs")

def job_list(request):
    job_list=Job.objects.all()
    
    context = {'job_list':job_list}
    return  render(request, 'job_list.html', context)


def job_list_form(request):
    if request.method == 'POST':
        form = JobForm(request.POST,request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.active_status = 1
            job.executed_date = '1900-01-01'
            job.complited_date = '1900-01-01'
            job.save()
            print("success")
            return redirect(reverse('jobs:joblist'))
        else:
            print("fail")
    
    form = JobForm()
    context = {'form': form}        
    return render(request, 'form.html',context)


def job_list_update_form(request,id):
    instance = get_object_or_404(Job, pk=id)
    form = JobForm(instance=instance)
    context = {'form': form}        
    
    if request.method == 'POST':
        form = JobForm(data=request.POST,instance=instance)
        if form.is_valid():
            instance.s_word = form.cleaned_data['s_word']
            instance.media = form.cleaned_data['media']
            instance.active_status = 1
            instance.executed_date = '1900-01-01'
            instance.complited_date = '1900-01-01'
            instance.t_st_date = form.cleaned_data['t_st_date']
            instance.t_end_date = form.cleaned_data['t_end_date']
            instance.save()
            return redirect(reverse('jobs:joblist'))
        else:
            return HttpResponse("입력 실패")
    return render(request, 'form.html',context)


def job_del(request,id):
    instance = get_object_or_404(Job, pk=id)
    
    print(instance)
    # print(request.GET.get('id'))
    instance.delete()

    return redirect(reverse('jobs:joblist'))


def target_list(request):
    target_list=Target_list.objects.all()

    context = {'target_list':target_list}
    # print(context)
    return render(request, 'target_list.html', context)


def target_del(request,id):
    t_instance = get_object_or_404(Target_list, pk=id)
    
    print(t_instance)
    # print(request.GET.get('id'))
    t_instance.delete()

    return redirect(reverse('jobs:targetlist'))

def target_list_form(request):
    if request.method == 'POST':
        form = Target_list_Form(request.POST,request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.active_status = 1
            job.executed_date = '1900-01-01'
            job.complited_date = '1900-01-01'
            job.save()
            print("success")
            return redirect(reverse('jobs:targetlist'))
        else:
            print("fail")
    
    form = Target_list_Form()
    context = {'form': form}        
    return render(request, 'form.html',context)
    # return HttpResponse("This is Target_list view")



def target_list_update_form(request,id):
    instance = get_object_or_404(Target_list, pk=id)
    form = Target_list_Form(instance=instance)
    context = {'form': form}        
    if request.method == 'POST':
        form = Target_list_Form(data=request.POST,instance=instance)
        if form.is_valid():
            instance.active_status = form.cleaned_data['media']
            instance.executed_date = form.cleaned_data['crawling_url']
            instance.complited_date = form.cleaned_data['input_col']
            instance.save()
            return redirect(reverse('jobs:targetlist'))
        else:
            return HttpResponse("입력 실패")
    print(form)
    return render(request, 'form.html',context)