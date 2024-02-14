from datetime import timedelta
from django.db import models
from users.models import NULLABLE, User


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE, verbose_name='Пользователь')
    place = models.CharField(max_length=255, **NULLABLE, verbose_name='Место')
    time = models.TimeField(verbose_name='Время', **NULLABLE)
    action = models.CharField(max_length=200, verbose_name='Действие', **NULLABLE)
    is_pleasant = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Связанная привычка')
    frequency = models.IntegerField(default=1, verbose_name='Периодичность')
    reward = models.CharField(max_length=150, verbose_name='Вознаграждение', **NULLABLE)
    execution_time = models.TimeField(default=timedelta(minutes=2), verbose_name='Время на выполнение', **NULLABLE)
    is_publication = models.BooleanField(default=True, verbose_name='Признак публичности')

    class Meta:
        verbose_name = 'Приятная привычка'
        verbose_name_plural = 'Приятные привычки'

    def __str__(self):
        return f'{self.user} будет {self.action} в {self.time} в {self.place}'
