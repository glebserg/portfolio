# Generated by Django 2.2 on 2021-05-01 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0008_auto_20210501_1934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='news_t',
            new_name='news',
        ),
    ]
