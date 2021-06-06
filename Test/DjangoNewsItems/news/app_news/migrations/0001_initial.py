# Generated by Django 2.2 on 2021-04-27 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('content', models.CharField(max_length=1000, verbose_name='Содержание')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('edit_date', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата редактирования')),
                ('flag_active', models.CharField(max_length=20, verbose_name='Флаг активности')),
            ],
            options={
                'db_table': 'news_item',
                'ordering': ['create_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_master', models.CharField(max_length=100, verbose_name='Имя пользователя')),
                ('text', models.CharField(max_length=300, verbose_name='Текст комментария')),
                ('news', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_news.NewsItem')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]