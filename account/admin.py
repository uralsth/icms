from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .models import Profile
from .models import CustomUser, Staff, Complainant

# Register your models here.
# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'photo')
#     list_editable = ['phone_number','photo']
#         return f'Profile for user {self.user.username}'

# class CustomUserAdmin(UserAdmin):
#     fieldsets = (
#         *UserAdmin.fieldsets,
#         (
#          'Additonal Info',
#          {
#           'fields':('phone_number', 'photo', 'address')

#           }
#          )
#     )

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
admin.site.register(Staff)
admin.site.register(Complainant)
