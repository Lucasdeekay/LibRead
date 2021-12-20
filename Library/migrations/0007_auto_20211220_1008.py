# Generated by Django 3.1.4 on 2021-12-20 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0006_auto_20211217_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ebook',
            name='is_approved',
        ),
        migrations.AddField(
            model_name='clientele',
            name='image',
            field=models.ImageField(null=True, upload_to='LibRead/profile-image'),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='file',
            field=models.FileField(upload_to='LibRead/ebooks/'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='file',
            field=models.FileField(upload_to='LibRead/journals/'),
        ),
    ]
