from django.db import models
from news.models import News


class Comments(models.Model):
    news_id = models.ForeignKey(News, blank=True, verbose_name="Новость",
                                on_delete=models.CASCADE, db_column="news_id")
    title = models.CharField(max_length= 50, verbose_name="Заголовок")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    comment = models.CharField(max_length=2000, verbose_name="Комментарий")
