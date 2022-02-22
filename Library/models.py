from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from Library.extra import ContentTypeRestrictedFileField


class Clientele(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=False)
    first_name = models.CharField(max_length=50, null=False)
    clientele_id = models.CharField(max_length=30, null=False)
    sex = models.CharField(max_length=10, null=False, choices=[('Male', 'Male'), ('Female', 'Female')])
    phone_no = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False)
    role = models.CharField(max_length=10, null=False, choices=[('Student', 'Student'), ('Staff', 'Staff'), ('Admin', 'Admin')])
    image = ContentTypeRestrictedFileField(upload_to='LibRead/profile-image',
                                           max_upload_size=5242880,
                                           content_types=['image/jpeg', 'image/jpg', 'image/png'],
                                           null=True,
                                           blank=True,
                                           max_length=250)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} -> {self.last_name} {self.first_name}"


class Password(models.Model):
    clientele = models.ForeignKey(Clientele, on_delete=models.CASCADE)
    recovery_password = models.CharField(max_length=12, null=False)
    time = models.DateTimeField(null=False)
    is_active = models.BooleanField(null=False, default=True)

    def __str__(self):
        return f"{self.clientele} -> {self.recovery_password}"

    def expiry(self):
        if (timezone.now() - self.time) >= timezone.timedelta(hours=1):
            self.delete()
        else:
            pass


class Ebook(models.Model):
    title = models.CharField(max_length=250, null=False)
    authors = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=250, null=False)
    date = models.DateTimeField(null=False)
    file = ContentTypeRestrictedFileField(upload_to="LibRead/ebooks/",
                                          max_upload_size=5242880,
                                          content_types=['application/pdf', 'application/zip'],
                                          null=False,
                                          max_length=250)

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
    authors = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=250, null=True)
    date = models.DateTimeField(null=False)
    file = ContentTypeRestrictedFileField(upload_to="LibRead/journals/",
                                          max_upload_size=5242880,
                                          content_types=['application/pdf', 'application/zip'],
                                          null=False,
                                          max_length=250)
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


class LibraryFile(models.Model):
    programme = models.CharField(max_length=250, null=False, choices=[
        ('Computer Science', 'Computer Science'),
        ('Software Engineering', 'Software Engineering'),
        ('Cyber Security', 'Cyber Security'),
        ('Biochemistry', 'Biochemistry'),
        ('Industrial Chemistry', 'Industrial Chemistry'),
        ('Business Administration', 'Business Administration'),
        ('Mass Communication', 'Mass Communication'),
        ('Criminology', 'Criminology'),
        ('Microbiology', 'Microbiology'),
        ('Economics', 'Economics'),
        ('Accounting', 'Accounting'),
    ])
    ebook = models.ManyToManyField(Ebook)
    journal = models.ManyToManyField(Journal)

    def __str__(self):
        return self.programme

