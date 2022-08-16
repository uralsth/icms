from django.shortcuts import render
from .forms import UserRegistrationForm, StaffRegistrationForm
from django.contrib.admin.views.decorators import staff_member_required

# from .models import Profile

# Create your views here.


def register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        # if user_form.is_valid() and profile_form.is_valid():
        if user_form.is_valid():
            # create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # set the chosen password
            new_user.set_password(user_form.cleaned_data["password"])
            # save the User and profile object
            new_user.save()
            # Profile.objects.create(user=new_user)
            return render(request, "account/register_done.html", {"new_user": new_user})
    else:
        user_form = UserRegistrationForm()
    # return render(request, 'account/register.html', {'user_form': user_form, 'profile_form': profile_form})
    return render(request, "account/register.html", {"user_form": user_form})

@staff_member_required
def staffregister(request):
    if request.method == "POST":
        user_form = StaffRegistrationForm(request.POST)
        # if user_form.is_valid() and profile_form.is_valid():
        if user_form.is_valid():
            # create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # set the chosen password
            new_user.set_password(user_form.cleaned_data["password"])
            # save the User and profile object
            new_user.save()
            # Profile.objects.create(user=new_user)
            return render(request, "account/staff/register_done.html", {"new_user": new_user})
    else:
        user_form = StaffRegistrationForm()
    # return render(request, 'account/register.html', {'user_form': user_form, 'profile_form': profile_form})
    return render(request, "account/staff/register.html", {"user_form": user_form})
