from django.db import models

from Library.models import Clientele


class Blog(models.Model):
    title = models.CharField(max_length=100)
    article = models.CharField(max_length=1000)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='LibRead/images/')

    def __str__(self):
        return f'{self.title}'

    def draft(self):
        return self.article[:100]


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    clientele = models.ForeignKey(Clientele, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    date = models.DateTimeField()
