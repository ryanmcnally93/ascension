from django.urls import path
from . import views

urlpatterns = [
    path('', views.record_studio_home, name='record_studio_home'),
]
