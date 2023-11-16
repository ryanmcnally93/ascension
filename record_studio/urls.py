from django.urls import path
from . import views

urlpatterns = [
    path("", views.record_studio_home, name="record_studio_home"),
    path(
        "meet_the_enginners/",
        views.meet_the_engineers,
        name="meet_the_engineers",
    ),
]
