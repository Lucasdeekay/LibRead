# Generated by Django 3.1.4 on 2022-01-04 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0011_auto_20220102_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='password',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
