# Generated by Django 2.2 on 2021-04-28 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0003_auto_20210428_0857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='name_master',
            new_name='name_author',
        ),
    ]
