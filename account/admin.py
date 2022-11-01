from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .models import Profile
from .models import  CustomUser , StaffProfile, Complainant

fields = list(UserAdmin.fieldsets)
fields[1] = (
    "Personal Info",
    {
        "fields": (
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "photo",
            "address",
            'role',
        )
    },
)
UserAdmin.fieldsets = tuple(fields)

admin.site.register(CustomUser, UserAdmin)

@admin.register(StaffProfile)
class StaffAdmin(admin.ModelAdmin):
    exclude = ('user',)

@admin.register(Complainant)
class ComplainantAdmin(admin.ModelAdmin):
    exclude = ('role',)
