# Generated by Django 2.2 on 2021-05-25 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0017_auto_20210524_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='check_admin',
            field=models.BooleanField(default=True, verbose_name='Одобрено администратором'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=300, verbose_name='Текст комментария'),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='content',
            field=models.TextField(max_length=1000, verbose_name='Содержание'),
        ),
    ]
