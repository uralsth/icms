from django.contrib import admin
from .models import Complaint, Department, Staff

# Register your models here.
admin.site.register(Complaint)
admin.site.register(Department)
admin.site.register(Staff)
