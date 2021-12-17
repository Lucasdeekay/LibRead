from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from Library.models import Clientele


def home(request):
    context = {}
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = Clientele.objects.get(clientele_id=request.user.username)
        context = {'current_clientele': current_clientele}
    return render(request, 'library/library_home.html', context)


def about(request):
    context = {}
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = Clientele.objects.get(clientele_id=request.user.username)
        context = {'current_clientele': current_clientele}
    return render(request, 'library/about.html', context)


def contact(request):
    context = {}
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = Clientele.objects.get(clientele_id=request.user.username)
        context = {'current_clientele': current_clientele}
    return render(request, 'library/contact.html', context)


def log_in(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        return HttpResponseRedirect(reverse('Library:repository'))
    else:
        return render(request, 'library/login.html')


def process_login(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        return HttpResponseRedirect(reverse('Library:repository'))
    else:
        clientele_id = request.POST.get('clientele_id')
        password = request.POST.get('password')
        user = authenticate(request, username=clientele_id, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('Library:repository'))
        else:
            messages.error(request, "Invalid login details")
            return HttpResponseRedirect(reverse('Library:login'))


def forgotten_password(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        return HttpResponseRedirect(reverse('Library:repository'))
    else:
        return render(request, 'library/forgot_password.html')


def password_retrieval(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        return HttpResponseRedirect(reverse('Library:repository'))
    else:
        return render(request, 'library/password_retrieval.html')


def update_password(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        return HttpResponseRedirect(reverse('Library:repository'))
    else:
        return render(request, 'library/update_password.html')


def register(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        return HttpResponseRedirect(reverse('Library:repository'))
    else:
        return render(request, 'library/register.html')


def process_registration(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        return HttpResponseRedirect(reverse('Library:repository'))
    else:
        last_name = request.POST.get('last_name').capitalize()
        first_name = request.POST.get('first_name').capitalize()
        clientele_id = request.POST.get('clientele_id')
        sex = request.POST.get('sex').capitalize()
        phone_no = request.POST.get('phone_number')
        email = request.POST.get('email')
        role = request.POST.get('role').capitalize()
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        all_clienteles = Clientele.objects.all()

        for clientele in all_clienteles:
            if clientele_id == clientele.clientele_id:
                messages.error(request, "User ID already in use")
                return HttpResponseRedirect(reverse('Library:register'))
            elif email == clientele.email:
                messages.error(request, "Email already in use")
                return HttpResponseRedirect(reverse('Library:register'))
        else:
            if password == confirm_password and len(password) >= 8:
                user = User.objects.create_user(username=clientele_id, email=email, password=password, last_name=last_name, first_name=first_name)
                Clientele.objects.create(user=user, last_name=last_name, first_name=first_name, clientele_id=clientele_id, sex=sex,
                                         phone_no=phone_no, email=email, role=role)
                if role == 'Admin':
                    group = Group.objects.get(name='Admin')
                    user.groups.add(group)
                elif role == 'Staff':
                    group = Group.objects.get(name='Staff')
                    user.groups.add(group)
                elif role == 'Student':
                    group = Group.objects.get(name='Student')
                    user.groups.add(group)
                messages.success(request, "Registration successful")
                return HttpResponseRedirect(reverse('Library:login'))
            elif len(password) < 8:
                messages.error(request, "Password must be 8 characters or more")
                return HttpResponseRedirect(reverse('Library:register'))
            elif password != confirm_password:
                messages.error(request, "Password does not match")
                return HttpResponseRedirect(reverse('Library:register'))


def repository(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = Clientele.objects.get(clientele_id=request.user.username)
        return render(request, 'library/library_main.html', {'current_clientele': current_clientele})
    else:
        messages.error(request, 'Please login to have access')
        return HttpResponseRedirect(reverse('Library:login'))


def offline_resources(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = Clientele.objects.get(clientele_id=request.user.username)
        return render(request, 'library/offline_resources.html', {'current_clientele': current_clientele})
    else:
        messages.error(request, 'Please login to have access')
        return HttpResponseRedirect(reverse('Library:login'))


def library_admin(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        if (User.objects.filter(username=request.user.username, groups__name='Staff').exists()) or (User.objects.filter(username=request.user.username, groups__name='Admin').exists()):
            current_clientele = Clientele.objects.get(clientele_id=request.user.username)
            return render(request, 'library/library_admin.html', {'current_clientele': current_clientele})
        else:
            messages.error(request, 'Access only available to Staff and Admin')
            return HttpResponseRedirect(reverse('Library:home'))
    else:
        messages.error(request, 'Please login to have access')
        return HttpResponseRedirect(reverse('Library:login'))


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('Library:login'))

