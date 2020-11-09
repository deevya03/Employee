from django.shortcuts import render
from .models import Employee
from django.http import Http404, HttpResponse


# Create your views here.

def home(request):
    employees = Employee.objects.all()
    return render(request, 'employees/home.html', {'employees': employees})


def task_detail(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        raise Http404('Employee Not Found')

    return render(request, 'employees/task-.html', {'employee': employee})


def search(request):
    return HttpResponse('This is search page.')
