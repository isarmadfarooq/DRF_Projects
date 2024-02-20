from django.contrib import admin
from .models import Employee, AttendenceRecord

# Define admin class for Employee model
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture']

# Define admin class for AttendenceRecord model
class AttendenceRecordAdmin(admin.ModelAdmin):
    list_display = ['employee_name', 'time_stamp']

# Register models and admin classes
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(AttendenceRecord, AttendenceRecordAdmin)
