from django.contrib import admin
from .models import EmployeeRecords, EmployeePreviousExperience

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id','employee_name','designation')
    search_fields = ("employee_name",)
    list_filter = ('employee_name',)
admin.site.register(EmployeeRecords, EmployeeAdmin)
admin.site.register(EmployeePreviousExperience)