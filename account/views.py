from django.shortcuts import render
from .forms import UserRegistrationForm, StaffRegistrationForm
from django.contrib.admin.views.decorators import staff_member_required

def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            return render(request, "account/register_done.html", {"new_user": new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, "account/register.html", {"user_form": user_form})

@staff_member_required
def staffregister(request):
    if request.method == "POST":
        user_form = StaffRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            return render(request, "account/staff/register_done.html", {"new_user": new_user})
    else:
        user_form = StaffRegistrationForm()
    return render(request, "account/staff/register.html", {"user_form": user_form})
