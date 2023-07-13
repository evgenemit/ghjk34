from django.db import models


class Record(models.Model):

    name = models.CharField(max_length=49, verbose_name='Название')
    date = models.DateTimeField(verbose_name='Дата и время')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
