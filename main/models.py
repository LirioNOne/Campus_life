from django.db import models


class News(models.Model):
    news_name = models.CharField('Заголовок', max_length=200)
    news_text = models.TextField('Текст новости')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.news_name

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
