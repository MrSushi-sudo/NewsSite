from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.TextField(max_length=200)
    publication_date = models.DateTimeField('Date Published')
    body_text = models.TextField('Body')
    image = models.ImageField(upload_to='news', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.pk})
