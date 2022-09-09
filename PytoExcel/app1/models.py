from django.db import models


class Generate_timesheet(models.Model):
    employee_name = models.CharField(max_length=30)
    client_name = models.CharField(max_length=20)
    project_manager = models.CharField(max_length=20)
    month_data = models.PositiveIntegerField(default=1, null=True, blank=True)
    year_data = models.PositiveIntegerField(default=2022, null=True, blank=True)
    leave_taken = models.DateField(default="2022-01-01", null=True, blank=True)
    holidays = models.DateField(default="2022-01-01", null=True, blank=True)
    extra_work = models.DateField(default="2022-01-01", null=True, blank=True)

    def __str__(self):
        return self.employee_name

