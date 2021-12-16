# Generated by Django 3.1.4 on 2021-12-16 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0003_auto_20211216_0915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('authors', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=250, null=True)),
                ('date', models.DateTimeField()),
                ('file', models.FileField(upload_to='ebooks/')),
            ],
        ),
    ]