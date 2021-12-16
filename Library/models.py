from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Clientele(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    matric_no = models.CharField(max_length=25)
    sex = models.CharField(max_length=6)
    phone_no = models.CharField(max_length=20)
    email = models.EmailField()
    role = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user} -> {self.last_name} {self.first_name}"


class Password(models.Model):
    clientele = models.ForeignKey(Clientele, on_delete=models.CASCADE)
    recovery_password = models.CharField(max_length=25)
    time = models.DateTimeField()

    def __str__(self):
        return f"{self.clientele} -> {self.recovery_password}"


class Ebook(models.Model):
    title = models.CharField(max_length=250)
    authors = models.CharField(max_length=500)
    description = models.CharField(max_length=250)
    programme = models.CharField(max_length=250)
    date = models.DateTimeField()
    file = models.FileField(upload_to="ebooks/")

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
