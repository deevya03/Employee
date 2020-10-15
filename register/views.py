from django.shortcuts import render,redirect
from .forms import RegistrationForm

from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == "POST":
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully!')
            fm.save()
            return redirect("loginPage")
    else:
        fm = RegistrationForm()
    return render(request, 'register/register.html', {'form': fm})
