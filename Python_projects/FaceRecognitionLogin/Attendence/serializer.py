from rest_framework import serializers
from .models import Employee, AttendenceRecord

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AttendenceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendenceRecord
        fields = ['id', 'employee_name', 'time_stamp']