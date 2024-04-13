from django.db import models


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    body = models.CharField(max_length=2000, verbose_name="Текст")
    deleted = models.BooleanField(default=False)
