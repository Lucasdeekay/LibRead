# Generated by Django 3.1.4 on 2021-12-16 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0002_auto_20211216_0953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientele',
            old_name='matric_no',
            new_name='clientele_id',
        ),
    ]
