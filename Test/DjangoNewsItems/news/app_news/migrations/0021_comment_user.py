# Generated by Django 2.2 on 2021-05-27 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_news', '0020_auto_20210527_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]