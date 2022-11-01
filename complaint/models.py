from django.db import models
from django.db.models.fields import timezone
from django.urls import reverse

# from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey

# from account.models import ComplainantProfile, StaffProfile
import account.models

class SolvedManager(models.Manager):
    def get_queryset(self):
        return super(SolvedManager, self).get_queryset().filter(status="solved")


class Department(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Complaint(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("solved", "Solved"),
    )

    complainant = models.ForeignKey(
        "account.ComplainantProfile", on_delete=models.CASCADE, related_name="complainant"
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique_for_date="created")
    complain = models.TextField()
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="to_department"
    )
    assigned_to = ChainedForeignKey(
        "account.StaffProfile",
        chained_field="department",
        chained_model_field="department",
        blank=True,
        show_all=False,
        auto_choose=False,
        sort=True,
    )
    address = models.CharField(max_length=250)
    updates = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    solved = SolvedManager()

    class Meta:
        ordering = ("-created",)

    def get_absolute_url(self):
        return reverse(
            "complaint:complaint_detail",
            args=[self.created.year, self.created.month, self.created.day, self.slug],
        )

    def __str__(self):
        return self.title
