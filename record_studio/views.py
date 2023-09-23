from django.shortcuts import render


def record_studio_home(request):
    return render(request, 'record_studio/home.html')


def meet_the_engineers(request):
    return render(request, 'record_studio/meet_the_engineers.html')
