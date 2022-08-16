from django import forms

# from django.contrib.auth.models import User
from .models import Staff, Complainant

# from phonenumber_field.modelfields import PhoneNumberField


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = Complainant
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "photo",
            "address",
            "phone_number",
        )
        # fields = "__all__"
        help_texts = {
            "username": None,
            # 'password1': None,
            # 'password2': None,
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Password don't match.")
        return cd["password2"]


class StaffRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = Staff
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "photo",
            "address",
            "phone_number",
        )
        # fields = "__all__"
        help_texts = {
            "username": None,
            # 'password1': None,
            # 'password2': None,
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Password don't match.")
        return cd["password2"]

# class ExtraUserRegistrationForm(forms.ModelForm):

# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')


# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ('phone_number', 'address', 'photo')
