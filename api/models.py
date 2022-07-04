from django.db import models


class Data(models.Model):
    result = models.JSONField('Город', null=True)

    def __str__(self):
        return f'{self.result["result"]}'

    class Meta:
        verbose_name_plural = 'Поиск'
