# Generated by Django 3.1.4 on 2022-01-13 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0013_auto_20220104_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]