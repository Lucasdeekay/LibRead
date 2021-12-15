from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'library/library_home.html')


def about(request):
    return render(request, 'library/about.html')


def contact(request):
    return render(request, 'library/contact.html')


def login(request):
    return render(request, 'library/login.html')


def forgotten_password(request):
    return render(request, 'library/forgot_password.html')


def password_retrieval(request):
    return render(request, 'library/password_retrieval.html')


def register(request):
    return render(request, 'library/register.html')


def repository(request):
    return render(request, 'library/library_main.html')


def offline_resources(request):
    return render(request, 'library/offline_resources.html')

