from django.db import models
from django.utils import timezone


class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    Departments = [
        ('s', 'Select'),
        ('d1', 'Development'),
        ('d2', 'Researcher'),
        ('d3', 'Administrative')
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email_id = models.EmailField(max_length=255)
    phone_num = models.CharField(max_length=13)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, default='M')
    date_of_birth = models.DateField()
    department = models.CharField(choices=Departments, max_length=10, default='s')
    employee_address = models.CharField(max_length=200)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name


class Task(models.Model):
    Supervisor = [
        ('s', 'Choose'),
        ('A', 'A'),
        ('d2', 'B'),
        ('d3', 'C')
    ]
    Task_Urgency = [
        ('L', 'Low'),
        ('N', 'Normal'),
        ('H', 'High')
    ]

    email_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # project_name = models.CharField(max_length=100)
    task_name = models.CharField(max_length=100)
    task_details = models.TextField(default='Add task Details', null=True)
    supervisor = models.CharField(choices=Supervisor, max_length=10, default='s')
    task_urgency = models.CharField(choices=Task_Urgency, max_length=1, default='L')
    task_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name


# class Department(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
