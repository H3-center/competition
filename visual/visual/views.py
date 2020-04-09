from django.shortcuts import render
from django.http import HttpResponse
from Jobs.models import Job


from module.monitor import get_statistics,findProcessIdByName
# Create your views here.
def main(request):
    # statistics=get_statistics()
    # print(statistics)
    result = findProcessIdByName('exe')
    print(result)
    return render(request, 'base.html')


def monitorring(request):
    statistics=get_statistics()
    print(statistics)
    return render(request, 'base.html')