# Generated by Django 2.2 on 2021-05-27 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0019_auto_20210527_0927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
