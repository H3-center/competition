from django.shortcuts import render
from django.http import HttpResponse
from Jobs.models import Job

# Create your views here.
def main(request):
    q_list = Job.objects.all()
    print(q_list)
    context = {'q_list': q_list}

    return render(request, 'job_list.html', context)
# all_jobs=Job.objects.all()
    
#     return render(request, 'jobs_list.html', {"all_jobs":all_jobs})

    # return HttpResponse("Hello This is Main")



    

