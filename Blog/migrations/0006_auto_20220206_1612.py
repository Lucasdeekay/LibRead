# Generated by Django 3.1.4 on 2022-02-06 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_auto_20220206_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='comment',
            field=models.ManyToManyField(to='Blog.Comment'),
        ),
        migrations.DeleteModel(
            name='BlogComment',
        ),
    ]