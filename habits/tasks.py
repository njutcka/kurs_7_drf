import requests
from django.conf import settings

from config.settings import TELEGRAM_TOKEN
from habits.models import Habit
import os
from datetime import timedelta, datetime

from celery import shared_task
from django.utils import timezone


def send_telegram_message(telegram_id, message):
    api_url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    params = {'telegram_id': telegram_id, 'text': message}

    response = requests.post(api_url, params=params)
    return response.json()


@shared_task
def send_habit_notification():
    now_time = timezone.now() + timedelta(hours=3)
    habits_to_send = Habit.objects.filter(user__telegram_id__isnull=False).prefetch_related('user')

    for habit in habits_to_send:
        habit_time = datetime.combine(now_time.date(), habit.time)
        habit_time_aware = timezone.make_aware(habit_time, now_time.tzinfo)

        if habit_time_aware <= now_time - timedelta(minutes=1):
            message = (f'Привет {habit.user}! Время {habit.time}. Пора идти в {habit.place} и сделать {habit.action}. ' \
                       f'Это займет {habit.execution_time } минут!')
            send_telegram_message(telegram_id=habit.user.telegram_id, message=message)
