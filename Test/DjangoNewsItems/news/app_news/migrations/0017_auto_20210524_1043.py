# Generated by Django 2.2 on 2021-05-24 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0016_auto_20210524_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='was_deleted',
        ),
        migrations.AddField(
            model_name='comment',
            name='check_admin',
            field=models.BooleanField(default=True, verbose_name='Удалено администратором'),
        ),
    ]
