import random
import string

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from DU_E_Library.settings import EMAIL_HOST_USER
from Library.models import Clientele, Password

random = random.Random()


def home(request):
    context = {}
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele}
    return render(request, 'library/library_home.html', context)


def about(request):
    context = {}
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele}
    return render(request, 'library/about.html', context)


def contact(request):
    context = {}
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
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


def send_recovery_pin(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        return HttpResponseRedirect(reverse('Library:repository'))
    else:
        clientele_id = request.POST.get('clientele_id')
        email = request.POST.get('email')
        all_user = User.objects.all()
        for user in all_user:
            if user.username == clientele_id and user.email == email:
                recovery_password = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(12)])
                subject = 'Password Recovery'
                Password.objects.create(clientele=Clientele.objects.get(user=user), recovery_pin=recovery_password, time=timezone.now())
                send_mail(subject, recovery_password, EMAIL_HOST_USER, [email], fail_silently=False)
                return HttpResponseRedirect(reverse('Library:password_retrieval', args=(user,)))
        else:
            messages.error(request, "User profile not found")
            return HttpResponseRedirect(reverse('Library:forgot_password'))


def password_retrieval(request, user):
    if request.user.is_authenticated and not request.user.is_superuser:
        return HttpResponseRedirect(reverse('Library:repository'))
    else:
        return render(request, 'library/password_retrieval.html', {'user': user})


def process_recovery_password(request, user):
    if request.user.is_authenticated and not request.user.is_superuser:
        return HttpResponseRedirect(reverse('Library:repository'))
    else:
        password = request.POST.get('password')
        clientele = get_object_or_404(Clientele, user=user)
        all_password = Password.objects.all()
        for passcode in all_password:
            if passcode.clientele == clientele and passcode.password == password:
                subject = 'Password Recovery Successful'
                msg = "Account successfully retrieved"
                send_mail(subject, msg, EMAIL_HOST_USER, [user.email], fail_silently=False)
                return HttpResponseRedirect(reverse('Library:password_retrieval'))
        else:
            messages.error(request, "Incorrect recovery password. Click on resend to get the retrieval password again")
            return HttpResponseRedirect(reverse('Library:password_retrieval'))


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
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        return render(request, 'library/library_main.html', {'current_clientele': current_clientele})
    else:
        messages.error(request, 'Please login to have access')
        return HttpResponseRedirect(reverse('Library:login'))


def offline_resources(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        return render(request, 'library/offline_resources.html', {'current_clientele': current_clientele})
    else:
        messages.error(request, 'Please login to have access')
        return HttpResponseRedirect(reverse('Library:login'))


def library_admin(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        if (User.objects.filter(username=request.user.username, groups__name='Staff').exists()) or (User.objects.filter(username=request.user.username, groups__name='Admin').exists()):
            current_clientele =get_object_or_404(Clientele, clientele_id=request.user.username)
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

