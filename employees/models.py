from django.db import models
from django.utils import timezone


class Employee(models.Model):
    Task_Urgency = [
        ('L', 'Low'),
        ('N', 'Normal'),
        ('H', 'High')
    ]
    Departments = [
        ('s', 'Select'),
        ('d1', 'Development'),
        ('d2', 'Researcher'),
        ('d3', 'Administrative')
    ]
    Supervisor = [
        ('s', 'Choose'),
        ('A', 'A'),
        ('d2', 'B'),
        ('d3', 'C')
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email_id = models.EmailField(max_length=255)
    phone_num = models.CharField(max_length=13)
    department = models.CharField(choices=Departments, max_length=10, default='s')
    supervisor = models.CharField(choices=Supervisor, max_length=10, default='s')
    task_urgency = models.CharField(choices=Task_Urgency, max_length=1, default='L')
    employee_address = models.CharField(max_length=200)
    date_joined = models.DateTimeField(default=timezone.now)
    task_name = models.CharField(max_length=100)
    task_completed = models.BooleanField(default=False)
    task_details = models.TextField(default='Not Defined', null=True)

    def __str__(self):
        return self.first_name
