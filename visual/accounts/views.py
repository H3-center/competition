from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout

from .forms import SignupForm, LoginForm
 
 
def signup(request):
    if request.user.is_authenticated:
        logout(request)
    signupform = SignupForm()
    if request.method == "POST":
        signupform = SignupForm(request.POST, request.FILES)
        if signupform.is_valid():
            user = signupform.save(commit=False)
            user.email = signupform.cleaned_data['email']
            user.save()
 
            return HttpResponse('가입 성공')
 
    return render(request, "signup.html", {
        "signupform": signupform,
    })

def signin(request):
    if request.user.is_authenticated:
        return redirect(reverse('jobs:overview'))
    if request.method == "POST":
        form = LoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email = email, password = password)
        if user is not None:
            login(request,user)
            return redirect(reverse('jobs:overview'))
        else:
            return redirect(reverse('accounts:signin'))
    else:
        form = LoginForm()
        return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect(reverse('accounts:signin'))

