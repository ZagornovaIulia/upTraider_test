from django.db import models

class Todo(models.Model):
    title = models.CharField('Название задания', max_length=200)
    is_complete = models.BooleanField('Задание выполнено', default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title
