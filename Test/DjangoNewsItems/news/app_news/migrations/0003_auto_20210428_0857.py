# Generated by Django 2.2 on 2021-04-28 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0002_auto_20210427_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitem',
            name='edit_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата редактирования'),
        ),
    ]
