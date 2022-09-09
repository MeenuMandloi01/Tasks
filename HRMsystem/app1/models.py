from django.db import models

class HRregistration(models.Model):
    Hr_name = models.CharField(max_length=20)
    Hr_email = models.EmailField(max_length=20)
    Hr_password = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.Hr_name

class Employee(models.Model):
    emp_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=10)
    mobile = models.PositiveIntegerField(null=True)
    address = models.TextField(max_length=50)
    designation = models.CharField(max_length=20)
    department = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.emp_name


