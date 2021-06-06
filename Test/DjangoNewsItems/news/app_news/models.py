from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


class NewsItem(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(max_length=1000, verbose_name='Содержание')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    edit_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата редактирования')
    flag_active = models.BooleanField(verbose_name='Флаг активности')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        db_table = 'news_item'
        ordering = ['-create_date']


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username=None)[0]


class Comment(models.Model):
    name_author = models.CharField(max_length=100, verbose_name='Имя пользователя')
    news = models.ForeignKey('NewsItem', default=None, null=True, on_delete=models.CASCADE, verbose_name='Новость')
    text = models.TextField(max_length=300, verbose_name='Текст комментария')
    check_admin = models.BooleanField(verbose_name='Одобрено администратором', default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, blank=True, null=True,
                             unique=False, on_delete=models.SET_NULL, verbose_name='Логин')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        db_table = 'comment'
