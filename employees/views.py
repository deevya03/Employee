from django.shortcuts import render
from .models import Employee

from django.http import Http404, HttpResponse
from .forms import AddEmployee


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
    query = request.GET['query']
    employees_first_name = Employee.objects.filter(first_name__icontains=query)
    employees_last_name = Employee.objects.filter(last_name__icontains=query)
    employees = employees_first_name.union(employees_last_name)
    print(employees)
    return render(request, 'employees/search.html', {'employees': employees})


def add(request):
    context = {}
    # create object of form
    form = AddEmployee()
    # check if form data is valid
    print(form)

    return render(request, 'employees/add.html', {'form': form})
