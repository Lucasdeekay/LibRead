from http import HTTPStatus

from django.contrib.auth.models import User, Group
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from Blog.models import Blog, Comment
from Library.models import Clientele


class HomeViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Group.objects.create(name='Admin')
        Group.objects.create(name='Student')

        cls.clientele = Clientele.objects.create(last_name="Adekunle", first_name="Michael", clientele_id='0000',
                                                 sex="Male", phone_no="09036451726", email="lekan@...", role="Admin")
        user = User.objects.create_user(username="0000", email=cls.clientele.email,
                                        last_name=cls.clientele.last_name, first_name=cls.clientele.first_name,
                                        password=cls.clientele.last_name)
        user.save()
        cls.clientele.user = user
        cls.clientele.save()

        group = Group.objects.get(name='Student')
        group.user_set.add(user)

        for i in range(3):
            Blog.objects.create(title=f'Blog{i+1}', article='An article for your blog', date=timezone.now(),
                                image='Library/static/images/du logo.png')

    def test_url_exist(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_is_accessible_by_name(self):
        response = self.client.get(reverse('Blog:home'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_uses_correct_template(self):
        response = self.client.get(reverse('Blog:home'))
        self.assertTemplateUsed(response, 'blog/home.html')


class BlogPageViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Group.objects.create(name='Admin')
        Group.objects.create(name='Student')

        cls.clientele = Clientele.objects.create(last_name="Adekunle", first_name="Michael", clientele_id='0000',
                                                 sex="Male", phone_no="09036451726", email="lekan@...", role="Admin")
        user = User.objects.create_user(username="0000", email=cls.clientele.email,
                                        last_name=cls.clientele.last_name, first_name=cls.clientele.first_name,
                                        password=cls.clientele.last_name)
        user.save()
        cls.clientele.user = user
        cls.clientele.save()

        group = Group.objects.get(name='Student')
        group.user_set.add(user)

        comment = Comment.objects.create(clientele=cls.clientele, comment='An article for your blog', date=timezone.now())

        blog = Blog.objects.create(title='Blog', article='An article for your blog', date=timezone.now(),
                                   image='Library/static/images/du logo.png')
        blog.comment.add(comment)

    def test_user_is_logged_in(self):
        logged_in = self.client.login(username='0000', password='Adekunle')
        self.assertTrue(logged_in)

    def test_user_is_not_logged_in_with_fail_data(self):
        logged_in = self.client.login(username='fail', password='fail')
        self.assertFalse(logged_in)

    def test_url_exists(self):
        response = self.client.get(reverse('Blog:blog_page', args=('Blog',)))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_exists_after_login_with_correct_data(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get(reverse('Blog:blog_page', args=('Blog',)))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_is_accessible_by_name(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get(reverse('Blog:blog_page', args=('Blog',)))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_uses_correct_template(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get(reverse('Blog:blog_page', args=('Blog',)))
        self.assertTemplateUsed(response, 'blog/blog_page.html')

    def test_url_redirects_if_not_logged_in(self):
        response = self.client.get(reverse('Blog:blog_page', args=('Blog',)))
        self.assertRedirects(response, reverse('Library:login'))