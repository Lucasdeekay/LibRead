# Generated by Django 3.1.4 on 2021-12-21 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0009_auto_20211220_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientele',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6),
        ),
    ]