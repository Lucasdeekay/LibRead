from django.db import models

from Library.extra import ContentTypeRestrictedFileField
from Library.models import Clientele


class Comment(models.Model):
    clientele = models.ForeignKey(Clientele, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.comment}'


class Blog(models.Model):
    title = models.CharField(max_length=250)
    article = models.CharField(max_length=1000)
    date = models.DateTimeField()
    image = ContentTypeRestrictedFileField(upload_to='LibRead/images/',
                                           max_upload_size=5242880,
                                           content_types=['image/jpeg', 'image/jpg', 'image/png'],
                                           null=True,
                                           blank=True,
                                           max_length=250)
    comment = models.ManyToManyField(Comment)


    def __str__(self):
        return f'{self.title}'

    def draft(self):
        return self.article[:250]

