from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):
    return HttpResponse("This is homepage")


def user_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return HttpResponseRedirect('/profile')
    else:
        fm = AuthenticationForm()
    return render(request, 'login/login.html', {'form': fm})


# Profile

def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'login/profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login/')


# Logout

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')
