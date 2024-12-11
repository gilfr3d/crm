from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'department', 'designation', 'status', 'hire_date')
    search_fields = ('full_name', 'email', 'department')

