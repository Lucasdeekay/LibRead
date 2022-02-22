from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.utils import timezone

from Blog.models import Blog, Comment
from Library.models import Clientele


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
        self.assertEqual(max_length, 250)

    def test_article_label(self):
        blog = get_object_or_404(Blog, title='Blog')
        field_label = blog._meta.get_field('article').verbose_name
        self.assertEqual(field_label, 'article')

    def test_article_max_length(self):
        blog = get_object_or_404(Blog, title='Blog')
        max_length = blog._meta.get_field('article').max_length
        self.assertEqual(max_length, 1000)

    def test_date_label(self):
        blog = get_object_or_404(Blog, title='Blog')
        field_label = blog._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_image_label(self):
        blog = get_object_or_404(Blog, title='Blog')
        field_label = blog._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'image')

    def test_comment_label(self):
        blog_comment = get_object_or_404(Blog, title='Blog')
        field_label = blog_comment._meta.get_field('comment').verbose_name
        self.assertEqual(field_label, 'comment')


class CommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        clientele = Clientele.objects.create(last_name="Adekunle", first_name="Michael", clientele_id=0000,
                                             sex="Male", phone_no="09036451726", email="lekan@...", role="Admin")
        user = User.objects.create_user(username="Adekunle", email=clientele.email,
                                        last_name=clientele.last_name, first_name=clientele.first_name,
                                        password=clientele.last_name)
        user.save()
        clientele.user = user
        clientele.save()
        Comment.objects.create(clientele=clientele, comment='An article for your blog', date=timezone.now())

    def test_clientele_label(self):
        comment = get_object_or_404(Comment, comment='An article for your blog')
        field_label = comment._meta.get_field('clientele').verbose_name
        self.assertEqual(field_label, 'clientele')

    def test_comment_label(self):
        comment = get_object_or_404(Comment, comment='An article for your blog')
        field_label = comment._meta.get_field('comment').verbose_name
        self.assertEqual(field_label, 'comment')

    def test_comment_max_length(self):
        comment = get_object_or_404(Comment, comment='An article for your blog')
        max_length = comment._meta.get_field('comment').max_length
        self.assertEqual(max_length, 1000)

    def test_date_label(self):
        comment = get_object_or_404(Comment, comment='An article for your blog')
        field_label = comment._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

