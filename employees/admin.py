from django.contrib import admin

from .models import Employee, Task


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email_id', 'phone_num', 'department']
    list_filter = ('department',)
    search_fields = ('first_name',)


@admin.register(Task)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['email_id', 'task_name']


# @admin.register(Department)
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ['name']
