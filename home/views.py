from django.shortcuts import render


def index(request):
    on_profile_page = True

    contexts = {
        'on_profile_page': on_profile_page,
    }
    return render(request, 'home/index.html', contexts)


def about(request):
    return render(request, 'home/about.html')
