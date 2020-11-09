from django.contrib import admin

from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email_id', 'phone_num', 'department']
    list_filter = ('department',)
    search_fields = ('first_name',)
