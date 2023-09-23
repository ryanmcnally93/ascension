from django.shortcuts import render


def record_studio_home(request):
    return render(request, 'record_studio/home.html')
