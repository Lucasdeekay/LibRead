# Generated by Django 3.1.4 on 2022-01-15 15:45

import Library.extra
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0017_auto_20220115_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ebook',
            name='file',
            field=Library.extra.ContentTypeRestrictedFileField(max_length=250, upload_to='LibRead/ebooks/'),
        ),
        migrations.AlterField(
            model_name='journal',
            name='file',
            field=Library.extra.ContentTypeRestrictedFileField(max_length=250, upload_to='LibRead/journals/'),
        ),
    ]