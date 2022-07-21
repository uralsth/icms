from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=150)
    available = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="of_department")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Complaint(models.Model):
    complainant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="complainant")
    title = models.CharField(max_length=100)
    complain = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="to_department")
    assigned_to = ChainedForeignKey(Staff,
                                    chained_field="department",
                                    chained_model_field="department",
                                    blank=True,
                                    show_all=False,
                                    auto_choose=False,
                                    sort=True)
    address = models.CharField(max_length=250)
    updates = models.TextField()
    solved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
