from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Complaint

# Create your views here.


@login_required
def complaint_home(request):
    return render(request, "complaint/home.html", {"section": "home"})


def complaint_list(request):
    complaints = Complaint.objects.all()
    return render(request, "complaint/list.html", {"complaints": complaints})


def complaint_detail(request, year, month, day, complaint):
    complaint = get_object_or_404(
        Complaint,
        slug=complaint,
        created__year=year,
        created__month=month,
        created__day=day,
    )
    return render(request, "complaint/detail.html", {"complaint": complaint})
