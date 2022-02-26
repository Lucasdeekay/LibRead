import random
import string

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags

from Blog.models import Blog
from DU_E_Library.settings import EMAIL_HOST_USER
from Library.forms import RegistrationForm, LoginForm, ForgotPasswordForm, PasswordRetrievalForm, UpdatePasswordForm, \
    UpdateImageForm, EbookForm, JournalForm, BlogForm
from Library.models import Clientele, Password, Journal, Ebook, LibraryFile

random = random.Random()


def home(request):
    all_blogs = Blog.objects.all()
    context = {'all_blogs': all_blogs}
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele, 'all_blogs': all_blogs}
        return render(request, 'library/library_home.html', context)
    else:
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
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                clientele_id = form.cleaned_data['user_id'].strip()
                password = form.cleaned_data['password'].strip()
                user = authenticate(request, username=clientele_id, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Login successful")
                    return HttpResponseRedirect(reverse('Library:repository'))
                else:
                    messages.error(request, "Invalid login details")
                    return HttpResponseRedirect(reverse('Library:login'))
        else:
            form = LoginForm()
        return render(request, 'library/login.html', {'form': form})


def forgotten_password(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        return HttpResponseRedirect(reverse('Library:repository'))
    else:
        if request.method == 'POST':
            form = ForgotPasswordForm(request.POST)
            if form.is_valid():
                clientele_id = form.cleaned_data['user_id'].strip()
                email = form.cleaned_data['email'].strip()
                all_user = User.objects.all()
                for user in all_user:
                    if user.username == clientele_id and user.email == email:
                        clientele = Clientele.objects.get(user=user)
                        recovery_password = ''.join(
                            [random.choice(string.ascii_letters + string.digits) for i in range(12)])
                        subject = 'Password Recovery'

                        all_passwords = Password.objects.filter(is_active=True)
                        for password in all_passwords:
                            if password.clientele == clientele and password.is_active:
                                password.is_active = False
                                break

                        Password.objects.create(clientele=clientele, recovery_password=recovery_password,
                                                time=timezone.now())

                        msg = f"Recovery password will expire after an hour. Your password is displayed below"
                        context = {'subject': subject, 'msg': msg, 'recovery_password': recovery_password, 'id': clientele.id}
                        html_message = render_to_string('library/msg.html', context=context)

                        send_mail(subject, msg, EMAIL_HOST_USER, [email], html_message=html_message, fail_silently=False)

                        messages.success(request, "Recovery password has been successfully sent")
                        return HttpResponseRedirect(reverse('Library:password_retrieval', args=(clientele.id,)))
                else:
                    messages.error(request, "User profile not found")
                    return HttpResponseRedirect(reverse('Library:forgot_password'))
        else:
            form = ForgotPasswordForm()
        return render(request, 'library/forgot_password.html', {'form': form})


def password_retrieval(request, clientele_id):
    all_passwords = Password.objects.filter(is_active=True)
    for password in all_passwords:
        password.expiry()

    if request.user.is_authenticated and not request.user.is_superuser:
        return HttpResponseRedirect(reverse('Library:repository'))
    else:
        if request.method == 'POST':
            form = PasswordRetrievalForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data['password'].strip()
                all_password = Password.objects.all()
                clientele = get_object_or_404(Clientele, id=clientele_id)

                for passcode in all_password:
                    if passcode.clientele == clientele and passcode.recovery_password == password and passcode.is_active:
                        subject = 'Password Recovery Successful'
                        msg = "Account has been successfully recovered. Kindly proceed to update your password"
                        context = {'subject': subject, 'msg': msg}
                        html_message = render_to_string('library/msg.html', context=context)

                        send_mail(subject, msg, EMAIL_HOST_USER, [clientele.email], html_message=html_message,
                                  fail_silently=False)

                        messages.success(request, 'Account has been successfully recovered. Kindly update your password')
                        return HttpResponseRedirect(reverse('Library:update_password', args=(clientele_id,)))
                else:
                    messages.error(request,
                                   "Incorrect recovery password. Click on resend to get the retrieval password again")
                    return HttpResponseRedirect(reverse('Library:password_retrieval', args=(clientele_id,)))
        else:
            form = PasswordRetrievalForm()
        current_clientele = get_object_or_404(Clientele, id=clientele_id)
        context = {'current_clientele': current_clientele, 'clientele_id': clientele_id, 'form': form}
        return render(request, 'library/password_retrieval.html', context)


def update_password(request, clientele_id):
    if request.method == 'POST':
        form = UpdatePasswordForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data['password'].strip()
            password2 = form.cleaned_data['confirm_password'].strip()

            if password1 == password2:
                user = Clientele.objects.get(id=clientele_id).user
                user.set_password(password1)
                user.save()

                subject = 'Password Update Successful'
                msg = "Account password has  been successfully changed"
                context = {'subject': subject, 'msg': msg}
                html_message = render_to_string('library/msg.html', context=context)

                send_mail(subject, msg, EMAIL_HOST_USER, [user.email], html_message=html_message,
                          fail_silently=False)

                messages.success(request, 'Password successfully changed')
                return HttpResponseRedirect(reverse('Library:login'))
            else:
                messages.error(request, "Password does not match")
                return HttpResponseRedirect(reverse('Library:update_password', args=(clientele_id,)))
    else:
        form = UpdatePasswordForm()
    current_clientele = get_object_or_404(Clientele, id=clientele_id)
    context = {'current_clientele': current_clientele, 'clientele_id': clientele_id, 'form': form}
    return render(request, 'library/update_password.html', context)


def register(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        return HttpResponseRedirect(reverse('Library:repository'))
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                last_name = form.cleaned_data['last_name'].capitalize().strip()
                first_name = form.cleaned_data['first_name'].capitalize().strip()
                clientele_id = form.cleaned_data['user_id'].strip()
                sex = form.cleaned_data['sex'].capitalize().strip()
                phone_no = form.cleaned_data['phone_number'].strip()
                email = form.cleaned_data['email'].strip()
                role = form.cleaned_data['role'].capitalize().strip()

                all_clienteles = Clientele.objects.all()

                for clientele in all_clienteles:
                    if clientele_id == clientele.clientele_id:
                        messages.error(request, "User ID already in use")
                        return HttpResponseRedirect(reverse('Library:register'))
                    elif email == clientele.email:
                        messages.error(request, "Email already in use")
                        return HttpResponseRedirect(reverse('Library:register'))
                else:
                    Clientele.objects.create(last_name=last_name, first_name=first_name, clientele_id=clientele_id,
                                             sex=sex,
                                             phone_no=phone_no, email=email, role=role)

                    subject = 'Password Update Successful'
                    msg = "Registration successful. A mail of approval will be sent to your email when " \
                          "your registration has been approved, alongside your login details. Thank You."
                    context = {'subject': subject, 'msg': msg}
                    html_message = render_to_string('library/msg.html', context=context)

                    send_mail(subject, msg, EMAIL_HOST_USER, [email], html_message=html_message,
                              fail_silently=False)

                    messages.success(request,
                                     "Registration successful. A mail of approval will be sent to your email within "
                                     "the next 48hrs. Thank You.")
                    return HttpResponseRedirect(reverse('Library:home'))
        else:
            form = RegistrationForm()
        return render(request, 'library/signup.html', {'form': form})


def update_profile_image(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        if request.method == 'POST':
            form = UpdateImageForm(request.POST, request.FILES)
            if form.is_valid():
                image = form.cleaned_data['image']
                current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
                current_clientele.image = image
                current_clientele.save()
                messages.success(request, 'Profile picture updated successfully')
                return HttpResponseRedirect(reverse('Library:repository'))
        else:
            form = UpdateImageForm()
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)
        context = {'current_clientele': current_clientele, 'form': form}
        return render(request, 'library/update_profile_image.html', context)
    else:
        messages.error(request, 'Please login to have access')
        return HttpResponseRedirect(reverse('Library:login'))


def repository(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)

        all_ebooks = Ebook.objects.all().order_by('-date')
        approved_journals = Journal.objects.filter(is_approved=True).order_by('-date')

        if request.method == 'POST':
            programme = request.POST.get("programme")
            if programme == "All":
                return HttpResponseRedirect(reverse('Library:repository'))
            else:
                sorted_file = get_object_or_404(LibraryFile, programme=programme)
                all_ebooks = sorted_file.ebook.all().order_by('-date')
                approved_journals = sorted_file.journal.filter(is_approved=True).order_by('-date')

        ebook_paginator = Paginator(all_ebooks, 20)  # Show 20 ebooks per page.
        ebook_page_number = request.GET.get('page')  # Get each paginated pages
        ebook_obj = ebook_paginator.get_page(ebook_page_number)  # Insert the number of items into page

        journal_paginator = Paginator(approved_journals, 20)  # Show 20 journals per page.
        journal_page_number = request.GET.get('page-')  # Get each paginated pages
        journal_obj = journal_paginator.get_page(journal_page_number)  # Insert the number of items into page

        context = {'current_clientele': current_clientele, 'ebook_obj': ebook_obj, 'journal_obj': journal_obj}
        return render(request, 'library/repository.html', context)
    else:
        messages.error(request, 'Please login to have access')
        return HttpResponseRedirect(reverse('Library:login'))


def library_admin(request):
    if request.user.is_authenticated and not request.user.is_superuser:
        if (User.objects.filter(username=request.user.username, groups__name='Staff').exists()) or (User.objects.filter(username=request.user.username, groups__name='Admin').exists()):
            current_clientele = get_object_or_404(Clientele, clientele_id=request.user.username)

            unauthorized_clienteles = Clientele.objects.filter(is_approved=False).order_by('-last_name')
            clientele_paginator = Paginator(unauthorized_clienteles, 20)  # Show 20 ebooks per page.
            clientele_page_number = request.GET.get('page')  # Get each paginated pages
            clientele_obj = clientele_paginator.get_page(clientele_page_number)  # Insert the number of items into page

            unauthorized_journals = Journal.objects.filter(is_approved=False).order_by('-date')
            journal_paginator = Paginator(unauthorized_journals, 20)  # Show 20 ebooks per page.
            journal_page_number = request.GET.get('page')  # Get each paginated pages
            journal_obj = journal_paginator.get_page(journal_page_number)  # Insert the number of items into page

            if request.method == 'POST':
                ebook_form = EbookForm(request.POST, request.FILES)
                journal_form = JournalForm(request.POST, request.FILES)
                blog_form = BlogForm(request.POST, request.FILES)
                if ebook_form.is_valid():
                    title = ebook_form.cleaned_data['title'].strip()
                    authors = ebook_form.cleaned_data['authors'].strip()
                    description = ebook_form.cleaned_data['description'].strip()
                    programme = ebook_form.cleaned_data['programme'].strip()
                    file = ebook_form.cleaned_data['file']
                    ebook = Ebook.objects.create(title=title, authors=authors, description=description, file=file,
                                                 date=timezone.now())
                    library_file = get_object_or_404(LibraryFile, programme=programme)
                    library_file.ebook.add(ebook)

                    messages.success(request, 'Ebook successfully uploaded')
                    return HttpResponseRedirect(reverse('Library:library_admin'))
                elif journal_form.is_valid():
                    title = journal_form.cleaned_data['title'].strip()
                    authors = journal_form.cleaned_data['authors'].strip()
                    description = journal_form.cleaned_data['description'].strip()
                    programme = ebook_form.cleaned_data['programme'].strip()
                    file = journal_form.cleaned_data['file']
                    journal = Journal.objects.create(title=title, authors=authors, description=description, file=file,
                                           date=timezone.now())
                    library_file = get_object_or_404(LibraryFile, programme=programme)
                    library_file.ebook.add(journal)

                    messages.success(request, 'Journal successfully uploaded and awaiting approval')
                    return HttpResponseRedirect(reverse('Library:library_admin'))
                elif blog_form.is_valid():
                    title = blog_form.cleaned_data['title'].strip()
                    article = blog_form.cleaned_data['article'].strip()
                    image = blog_form.cleaned_data['image']
                    Blog.objects.create(title=title, article=article, image=image, date=timezone.now())
                    messages.success(request, 'Blog successfully uploaded')
                    return HttpResponseRedirect(reverse('Library:library_admin'))
            else:
                ebook_form = EbookForm()
                journal_form = JournalForm()
                blog_form = BlogForm()
            context = {
                'current_clientele': current_clientele,
                'unauthorized_clienteles': unauthorized_clienteles,
                'unauthorized_journals': unauthorized_journals,
                'ebook_form': ebook_form,
                'journal_form': journal_form,
                'blog_form': blog_form,
                'clientele_obj': clientele_obj,
                'journal_obj': journal_obj,
            }
            return render(request, 'library/library_admin.html', context)
        else:
            messages.error(request, 'Access only available to Staff and Admin')
            return HttpResponseRedirect(reverse('Library:home'))
    else:
        messages.error(request, 'Please login to have access')
        return HttpResponseRedirect(reverse('Library:login'))


def approve_clientele(request, clientele_id):
    current_clientele = get_object_or_404(Clientele, id=clientele_id)
    current_clientele.is_approved = True

    current_clientele.save()
    messages.success(request, f"{current_clientele.last_name} {current_clientele.first_name} has been successfully authorized")

    password = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(10)])
    user = User.objects.create_user(username=current_clientele.clientele_id, email=current_clientele.email, password=password,
                                    last_name=current_clientele.last_name, first_name=current_clientele.first_name)
    current_clientele.user = user
    current_clientele.save()
    if current_clientele.role == 'Admin':
        group = Group.objects.get(name='Admin')
        user.groups.add(group)
    elif current_clientele.role == 'Staff':
        group = Group.objects.get(name='Staff')
        user.groups.add(group)
    elif current_clientele.role == 'Student':
        group = Group.objects.get(name='Student')
        user.groups.add(group)

    subject = 'Registration Approval'
    msg = f"You have been successfully approved to make use of Dominion university library. Kindly proceed to update " \
          f"after login. Your password is displayed below"
    context = {'subject': subject, 'msg': msg, 'password': password}
    html_message = render_to_string('library/msg.html', context=context)
    plain_message = f"You have been successfully approved to make use of Dominion university library. Kindly proceed to update " \
                    f"after login. Your password is {password}"

    send_mail(subject, plain_message, EMAIL_HOST_USER, [current_clientele.email], html_message=html_message,
              fail_silently=False)

    return HttpResponseRedirect(reverse('Library:library_admin'))


def reject_clientele(request, clientele_id):
    clientele = get_object_or_404(Clientele, id=clientele_id)
    clientele.delete()
    messages.success(request, f"{clientele.last_name} {clientele.first_name} registration has been rejected")

    subject = 'Invalid Registration'
    msg = f"Your registration to Dominion University library has been considered invalid and thereby, unapproved." \
          f" Kindly register again with valid information. Thank you"
    context = {'subject': subject, 'msg': msg}
    html_message = render_to_string('library/msg.html', context=context)

    send_mail(subject, msg, EMAIL_HOST_USER, [clientele.email], html_message=html_message,
              fail_silently=False)
    return HttpResponseRedirect(reverse('Library:library_admin'))


def approve_journal(request, journal_id):
    journal = get_object_or_404(Journal, id=journal_id)
    journal.is_approved = True
    journal.save()
    messages.success(request, f"{journal.title} by {journal.authors} has been successfully approved")
    return HttpResponseRedirect(reverse('Library:library_admin'))


def reject_journal(request, journal_id):
    journal = get_object_or_404(Journal, id=journal_id)
    journal.delete()
    messages.success(request, f"{journal.title} by {journal.authors} has been rejected")
    return HttpResponseRedirect(reverse('Library:library_admin'))


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

