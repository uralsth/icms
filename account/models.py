from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser, BaseUserManager
from complaint.models import Department
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
#     address = models.CharField(max_length=100, null=True, blank=True)
#     phone_number = PhoneNumberField(blank=True)
#     photo = models.ImageField(upload_to='users/%y/%m/%d', blank=True)

#     def __str__(self):


class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        COMPLAINANT = "COMPLAINANT", "Complainant"
        STAFF = "STAFF", "Staff"

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone_number = PhoneNumberField(blank=True)
    photo = models.ImageField(upload_to="users/%y/%m/%d", blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


class StaffManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.STAFF)


class Staff(CustomUser):
    base_role = CustomUser.Role.STAFF

    staff = StaffManager()

    class Meta:
        proxy = True

    def __str__(self):
        return self.username




class StaffProfile(models.Model):
    user = models.OneToOneField(Staff, on_delete=models.CASCADE)
    available = models.BooleanField(default=False)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="of_department", null=True, blank=True)
    # staff_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=Staff)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "STAFF":
        StaffProfile.objects.create(user=instance)

class ComplainantManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=CustomUser.Role.COMPLAINANT)


class Complainant(CustomUser):
    base_role = CustomUser.Role.COMPLAINANT

    complainant = ComplainantManager()

    class Meta:
        proxy = True

    def __str__(self):
        return self.username



class ComplainantProfile(models.Model):
    user = models.OneToOneField(Complainant, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=Complainant)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == "COMPLAINANT":
        ComplainantProfile.objects.create(user=instance)
