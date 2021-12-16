from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=250)
    article = models.CharField(max_length=1000)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.title}'
