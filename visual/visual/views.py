from django.shortcuts import render
from django.http import HttpResponse
from Jobs.models import Job
from module import mc

from module.monitor_linux import get_statistics,findProcessIdByName
# Create your views here.
def main(request):
    # statistics=get_statistics()
    # print(statistics)
    print("test 페이지 시작")
    # main(username, q, std, end):
    mc.main(request.user.name,"삼성","2001-01-01","2001-01-31")
    print("test 페이지 모듈 끝")
    # result = findProcessIdByName('exe')
    # print(result)
    return render(request, 'base.html')


def monitorring(request):
    statistics=get_statistics()
    print(statistics)
    return render(request, 'base.html')


