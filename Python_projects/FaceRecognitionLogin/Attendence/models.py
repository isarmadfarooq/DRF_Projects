from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="employee_images/")

class AttendenceRecord(models.Model):
    employee_name = models.CharField(max_length=100)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee_name} - {self.time_stamp}"