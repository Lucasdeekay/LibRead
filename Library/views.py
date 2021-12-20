import random
import string
from operator import attrgetter

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from Blog.models import Blog
from DU_E_Library.settings import EMAIL_HOST_USER
from Library.models import Clientele, Password, Journal, Ebook

random = random.Random()


def update_users():
    all_clienteles = Clientele.objects.all()
    all_users = User.objects.all()
    for clientele in all_clienteles:
        if clientele.is_approved:
            for user in all_users:
                if clientele.clientele_id == user.username:
                    break
            else:
                password = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(10)])
                user = User.objects.create_user(username=clientele.clientele_id, email=clientele.email, password=password, last_name=clientele.last_name, first_name=clientele.first_name)
                clientele.user = user
                clientele.save()
                if clientele.role == 'Admin':
                    group = Group.objects.get(name='Admin')
                    user.groups.add(group)
                elif clientele.role == 'Staff':
                    group = Group.objects.get(name='Staff')
                    user.groups.add(group)
                elif clientele.role == 'Student':
                    group = Group.objects.get(name='Student')
                    user.groups.add(group)

                subject = 'Registration Approval'
                msg = f"You have been successfully approved to make use of Dominion university library. Your password " \
                      f"is {password}. You can proceed to update after login"
                send_mail(subject, msg, EMAIL_HOST_USER, [clientele.email], fail_silently=False)
                return HttpResponseRedirect(reverse('Library:login'))


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
    context = {}
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele}
        return HttpResponseRedirect(reverse('Library:repository', args=(context,)))
    else:
        return render(request, 'library/login.html', context)


def process_login(request):
    context = {}
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele}
        return HttpResponseRedirect(reverse('Library:repository', args=(context, )))
    else:
        clientele_id = request.POST.get('clientele_id')
        password = request.POST.get('password')
        user = authenticate(request, username=clientele_id, password=password)
        if user is not None:
            login(request, user)
            current_clientele = get_object_or_404(Clientele, clientele_id=clientele_id)
            context = {'current_clientele': current_clientele}
            return HttpResponseRedirect(reverse('Library:repository', args=(context, )))
        else:
            messages.error(request, "Invalid login details")
            return HttpResponseRedirect(reverse('Library:login', args=(context, )))


def forgotten_password(request):
    context = {}
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele}
        return HttpResponseRedirect(reverse('Library:repository', args=(context,)))
    else:
        return render(request, 'library/forgot_password.html', context)


def send_recovery_pin(request):
    context = {}
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele}
        return HttpResponseRedirect(reverse('Library:repository', args=(context,)))
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

                current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
                context = {'current_clientele': current_clientele, 'username': user.username}

                return HttpResponseRedirect(reverse('Library:password_retrieval', args=(context,)))
        else:
            messages.error(request, "User profile not found")
            return HttpResponseRedirect(reverse('Library:forgot_password', args=(context, )))


def password_retrieval(request, username):
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele}
        return HttpResponseRedirect(reverse('Library:repository', args=(context,)))
    else:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele, 'username': username}
        return render(request, 'library/password_retrieval.html', context)


def process_recovery_password(request, username):
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele}
        return HttpResponseRedirect(reverse('Library:repository', args=(context, )))
    else:
        password = request.POST.get('password')
        clientele = get_object_or_404(Clientele, user=User.objects.get_by_natural_key(username=username))
        all_password = Password.objects.all()

        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele, 'username': username}

        for passcode in all_password:
            if passcode.clientele == clientele and passcode.password == password:
                subject = 'Password Recovery Successful'
                msg = "Account successfully retrieved"
                send_mail(subject, msg, EMAIL_HOST_USER, [clientele.email], fail_silently=False)
                return HttpResponseRedirect(reverse('Library:update_password', args=(context,)))
        else:
            messages.error(request, "Incorrect recovery password. Click on resend to get the retrieval password again")
            return HttpResponseRedirect(reverse('Library:password_retrieval', args=(context,)))


def update_password(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele, 'username': request.user.username}
        return render(request, 'library/update_password.html', context)
    else:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele}
        return HttpResponseRedirect(reverse('Library:login', args=(context,)))


def set_updated_password(request, username):
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele}
        return HttpResponseRedirect(reverse('Library:repository', args=(context,)))
    else:
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele, 'username': username}

        if password1 == password2:
            user = User.objects.get_by_natural_key(username=username)
            user.set_password(password1)
            user.save()
            subject = 'Password Update Successful'
            msg = "Account password has  been successfully changed"
            send_mail(subject, msg, EMAIL_HOST_USER, [user.email], fail_silently=False)
            return HttpResponseRedirect(reverse('Library:login', args=(context, )))
        else:
            messages.error(request, "Password does not match")
            return HttpResponseRedirect(reverse('Library:update_password', args=(context,)))


def register(request):
    context = {}
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele}
        return HttpResponseRedirect(reverse('Library:repository', args=(context,)))
    else:
        return render(request, 'library/register.html', context)


def process_registration(request):
    context = {}
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele}
        return HttpResponseRedirect(reverse('Library:repository', args=(context,)))
    else:
        last_name = request.POST.get('last_name').capitalize()
        first_name = request.POST.get('first_name').capitalize()
        clientele_id = request.POST.get('clientele_id')
        sex = request.POST.get('sex').capitalize()
        phone_no = request.POST.get('phone_number')
        email = request.POST.get('email')
        role = request.POST.get('role').capitalize()

        all_clienteles = Clientele.objects.all()

        for clientele in all_clienteles:
            if clientele_id == clientele.clientele_id:
                messages.error(request, "User ID already in use")
                return HttpResponseRedirect(reverse('Library:register', args=(context,)))
            elif email == clientele.email:
                messages.error(request, "Email already in use")
                return HttpResponseRedirect(reverse('Library:register', args=(context,)))
        else:
            Clientele.objects.create(last_name=last_name, first_name=first_name, clientele_id=clientele_id, sex=sex,
                                     phone_no=phone_no, email=email, role=role)

            messages.success(request, "Registration successful. A mail of approval will be sent to your email within "
                                      "the next 48hrs. Thank You.")
            return HttpResponseRedirect(reverse('Library:home', args=(context,)))


def update_profile_image(request):
    context = {}
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele}
        return render(request, 'library/upload_image.html', context)
    else:
        messages.error(request, 'Please login to have access')
        return HttpResponseRedirect(reverse('Library:login', args=(context,)))


def upload_image(request):
    context = {}
    if request.user.is_authenticated and not request.user.is_superuser:
        image = request.FILES.get('image')
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        current_clientele.image = image
        current_clientele.save()
        messages.success(request, 'Profile picture updated successfully')

        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele}

        return HttpResponseRedirect(reverse('Library:repository', args=(context,)))
    else:
        messages.error(request, 'Please login to have access')
        return HttpResponseRedirect(reverse('Library:login', args=(context,)))


def repository(request):
    context = {}
    update_users()
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele}
        return render(request, 'library/library_main.html', context)
    else:
        messages.error(request, 'Please login to have access')
        return HttpResponseRedirect(reverse('Library:login', args=(context,)))


def offline_resources(request):
    context = {}
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        all_ebooks = Ebook.objects.all()
        approved_journals = Journal.objects.filter(is_approved=True)
        e_list = [all_ebooks + approved_journals]
        e_list.sort()
        e_resources = sorted(e_list, key=attrgetter('date'))
        context = {'current_clientele': current_clientele, 'e_resources': e_resources}
        return render(request, 'library/offline_resources.html', context)
    else:
        messages.error(request, 'Please login to have access')
        return HttpResponseRedirect(reverse('Library:login', args=(context,)))


def library_admin(request):
    context = {}
    if request.user.is_authenticated and not request.user.is_superuser:
        if (User.objects.filter(username=request.user.username, groups__name='Staff').exists()) or (User.objects.filter(username=request.user.username, groups__name='Admin').exists()):
            current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
            unauthorized_clienteles = Clientele.objects.filter(status=False)
            unauthorized_journals = Journal.objects.filter(status=False)
            context = {'current_clientele': current_clientele, 'unauthorized_clienteles': unauthorized_clienteles, 'unauthorized_journals': unauthorized_journals}
            return render(request, 'library/library_admin.html', context)
        else:
            current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
            context = {'current_clientele': current_clientele}
            messages.error(request, 'Access only available to Staff and Admin')
            return HttpResponseRedirect(reverse('Library:home', args=(context,)))
    else:
        messages.error(request, 'Please login to have access')
        return HttpResponseRedirect(reverse('Library:login', args=(context,)))


def upload_ebook(request):
    title = request.POST.get('title')
    authors = request.POST.get('authors')
    description = request.POST.get('description')
    programme = request.POST.get('programme')
    file = request.FILES.get('file')
    Ebook.objects.create(title=title, authors=authors, description=description, programme=programme, file=file, date=timezone.now())
    messages.success(request, 'Ebook successfully uploaded')

    current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
    context = {'current_clientele': current_clientele}

    return HttpResponseRedirect(reverse('Library:library_admin', args=(context,)))


def upload_journal(request):
    title = request.POST.get('title')
    authors = request.POST.get('authors')
    description = request.POST.get('description')
    file = request.FILES.get('file')
    Journal.objects.create(title=title, authors=authors, description=description, file=file, date=timezone.now())
    messages.success(request, 'Journal successfully uploaded and awaiting approval')

    current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
    context = {'current_clientele': current_clientele}

    return HttpResponseRedirect(reverse('Library:library_admin', args=(context, )))


def upload_blog(request):
    title = request.POST.get('title')
    article = request.POST.get('article')
    image = request.FILES.get('image')
    Blog.objects.create(title=title, article=article, image=image, date=timezone.now())
    messages.success(request, 'Blog successfully uploaded')

    current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
    context = {'current_clientele': current_clientele}

    return HttpResponseRedirect(reverse('Library:library_admin', args=(context,)))


def approve_clientele(request, clientele_id):
    clientele = get_object_or_404(Clientele, id=clientele_id)
    clientele.is_approved = True
    clientele.save()
    messages.success(request, f"{clientele.last_name} {clientele.first_name} has been successfully authorized")

    current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
    context = {'current_clientele': current_clientele}

    return HttpResponseRedirect(reverse('Library:library_admin', args=(context,)))


def reject_clientele(request, clientele_id):
    clientele = get_object_or_404(Clientele, id=clientele_id)
    clientele.delete()
    messages.success(request, f"{clientele.last_name} {clientele.first_name} registration has been rejected")

    current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
    context = {'current_clientele': current_clientele}

    return HttpResponseRedirect(reverse('Library:library_admin', args=(context,)))


def approve_journal(request, journal_id):
    journal = get_object_or_404(Journal, id=journal_id)
    journal.is_approved = True
    journal.save()
    messages.success(request, f"{journal.title} by {journal.authors} has been successfully approved")

    current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
    context = {'current_clientele': current_clientele}

    return HttpResponseRedirect(reverse('Library:library_admin', args=(context,)))


def reject_journal(request, journal_id):
    journal = get_object_or_404(Journal, id=journal_id)
    journal.delete()
    messages.success(request, f"{journal.title} by {journal.authors} has been rejected")

    current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
    context = {'current_clientele': current_clientele}

    return HttpResponseRedirect(reverse('Library:library_admin', args=(context,)))


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('Library:login'))


def error_400(request, exception):
    return render(request, 'library/400.html')


def error_403(request, exception):
    return render(request, 'library/403.html')


def error_404(request, exception):
    return render(request, 'library/404.html')


def error_500(request):
    return render(request, 'library/500.html')

