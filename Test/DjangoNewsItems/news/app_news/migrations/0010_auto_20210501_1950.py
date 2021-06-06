# Generated by Django 2.2 on 2021-05-01 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0009_auto_20210501_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='news',
        ),
        migrations.AddField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_news.NewsItem'),
        ),
    ]