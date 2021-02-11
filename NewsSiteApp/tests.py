from django.test import TestCase
from django.urls import reverse

from .models import News


class NewsTests(TestCase):

    def setUp(self):
        self.news = News.objects.create(
            title='Тест',
            publication_date='2021-01-29 00:00:00',
            body_text='Тест',
            image='news/1.png',
        )

    def test_get_absolute_url(self):
        self.assertEqual(self.news.get_absolute_url(), '/news/1/')

    def test_news_content(self):
        self.assertEqual(f'{self.news.title}', 'Тест')
        self.assertEqual(f'{self.news.publication_date}', '2021-01-29 00:00:00')
        self.assertEqual(f'{self.news.body_text}', 'Тест')
        self.assertEqual(f'{self.news.image}', 'news/1.png')

    def test_news_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тест')
        self.assertTemplateUsed(response, 'home.html')

    def test_news_detail_view(self):
        response = self.client.get(f'/news/{self.news.pk}/')
        no_response = self.client.get('/news/55555/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Тест')
        self.assertTemplateUsed(response, 'news_detail.html')

    def test_news_create_view(self):
        response = self.client.post(reverse('news_create'), {
            'title': 'Тест 2',
            'publication_date': '2021-02-05 00:00:00',
            'body_text': 'Тестовое описание 2',
            'image': 'news/1.png',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(News.objects.count(), 2)
