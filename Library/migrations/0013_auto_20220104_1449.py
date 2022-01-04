# Generated by Django 3.1.4 on 2022-01-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0012_password_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='password',
            old_name='active',
            new_name='is_active',
        ),
        migrations.AlterField(
            model_name='clientele',
            name='clientele_id',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='clientele',
            name='role',
            field=models.CharField(choices=[('Student', 'Student'), ('Staff', 'Staff'), ('Admin', 'Admin')], max_length=10),
        ),
        migrations.AlterField(
            model_name='clientele',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='authors',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='programme',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='journal',
            name='authors',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='journal',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='password',
            name='recovery_password',
            field=models.CharField(max_length=12),
        ),
    ]