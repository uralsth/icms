from django.urls import path
from . import views

app_name = "complaint"

urlpatterns = [
    path("", views.complaint_home, name="home"),
    path("list", views.complaint_list, name="list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:complaint>/",
        views.complaint_detail,
        name="detail",
    ),
]
