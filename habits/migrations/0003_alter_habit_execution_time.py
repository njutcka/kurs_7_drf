# Generated by Django 4.2.7 on 2024-01-29 19:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_rename_owner_habit_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='execution_time',
            field=models.TimeField(blank=True, default=datetime.timedelta(seconds=120), null=True, verbose_name='Время на выполнение'),
        ),
    ]
