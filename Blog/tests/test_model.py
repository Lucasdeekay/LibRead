from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.utils import timezone

from Blog.models import Blog


class BlogModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Blog.objects.create(title='Blog', article='An article for your blog', date=timezone.now(),
                            image='Library/static/images/du logo.png')

    def test_title_label(self):
        blog = get_object_or_404(Blog, title='Blog')
        field_label = blog._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_max_length(self):
        blog = get_object_or_404(Blog, title='Blog')
        max_length = blog._meta.get_field('title').max_length
        self.assertEqual(max_length, 50)

    def test_article_label(self):
        blog = get_object_or_404(Blog, title='Blog')
        field_label = blog._meta.get_field('article').verbose_name
        self.assertEqual(field_label, 'article')

    def test_article_max_length(self):
        blog = get_object_or_404(Blog, title='Blog')
        max_length = blog._meta.get_field('article').max_length
        self.assertEqual(max_length, 300)

    def test_date_label(self):
        blog = get_object_or_404(Blog, title='Blog')
        field_label = blog._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_image_label(self):
        blog = get_object_or_404(Blog, title='Blog')
        field_label = blog._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'image')