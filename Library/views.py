from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'library/library_home.html')


def about(request):
    return render(request, 'library/about.html')


def contact(request):
    return render(request, 'library/contact.html')
