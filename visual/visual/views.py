from django.shortcuts import render
from django.http import HttpResponse
from Jobs.models import Job

# Create your views here.
def main(request):
    return render(request, 'base.html')
