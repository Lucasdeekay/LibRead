from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Clientele(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    last_name = models.CharField(max_length=50, null=False)
    first_name = models.CharField(max_length=50, null=False)
    clientele_id = models.CharField(max_length=25, null=False)
    sex = models.CharField(max_length=6, null=False, choices=[('male', 'Male'), ('female', 'Female')])
    phone_no = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False)
    role = models.CharField(max_length=15, null=False, choices=[('student', 'Student'), ('staff', 'Staff'), ('admin', 'Admin')])
    image = models.ImageField(upload_to='LibRead/profile-image', null=False)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} -> {self.last_name} {self.first_name}"


class Password(models.Model):
    clientele = models.ForeignKey(Clientele, on_delete=models.CASCADE)
    recovery_password = models.CharField(max_length=25, null=False)
    time = models.DateTimeField(null=False)

    def __str__(self):
        return f"{self.clientele} -> {self.recovery_password}"


class Ebook(models.Model):
    title = models.CharField(max_length=250, null=False)
    authors = models.CharField(max_length=500, null=False)
    description = models.CharField(max_length=250, null=False)
    programme = models.CharField(max_length=250, null=False)
    date = models.DateTimeField(null=False)
    file = models.FileField(upload_to="LibRead/ebooks/", null=False)

    def __str__(self):
        return f"{self.title} -> {self.authors}"

    def post_update(self):
        if (timezone.now() - self.date) < timezone.timedelta(days=1):
            return "recently posted"
        elif (timezone.now() - self.date) > timezone.timedelta(weeks=4):
            return "outdated post"
        else:
            return ""

    def duration_of_post(self):
        return timezone.now() - self.date


class Journal(models.Model):
    title = models.CharField(max_length=250, null=False)
    authors = models.CharField(max_length=500, null=False)
    description = models.CharField(max_length=250, null=True)
    date = models.DateTimeField(null=False)
    file = models.FileField(upload_to="LibRead/journals/", null=False)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} -> {self.authors}"

    def post_update(self):
        if (timezone.now() - self.date) < timezone.timedelta(days=1):
            return "recently posted"
        elif (timezone.now() - self.date) > timezone.timedelta(weeks=4):
            return "outdated post"
        else:
            return ""

    def duration_of_post(self):
        return timezone.now() - self.date
