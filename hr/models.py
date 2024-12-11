from django.db import models

class Employee(models.Model):
    full_name = models.CharField(max_length=100)  # Combined first and last name
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    hire_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])

    def __str__(self):
        return self.full_name

