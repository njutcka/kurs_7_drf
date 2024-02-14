from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPagination
from habits.permisions import IsOwner
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """ Создание привычки """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]



class HabitListAPIView(generics.ListAPIView):
    """ Вывод списка привычек пользователя """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """ Определяем параметры вывода объектов """

        queryset = Habit.objects.filter(user=self.request.user)
        return queryset


class HabitPublicListAPIView(generics.ListAPIView):
    """ Вывод списка публичных привычек """

    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        """ Определяем параметры вывода объектов """

        queryset = Habit.objects.filter(is_publication=True)
        return queryset


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр информации об одной привычке """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Изменение привычки """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_update(self, serializer):

        habit = serializer.save()
        habit.save()


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Удаление привычки """

    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_destroy(self, instance):

        instance.delete()
