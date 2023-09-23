from django.shortcuts import render


def rehearse_home(request):
    return render(request, 'rehearse/home.html')
