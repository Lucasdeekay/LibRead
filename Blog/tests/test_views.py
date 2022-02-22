from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from Blog.models import Blog, Comment
from Library.models import Clientele


class HomeViewTest(TestCase):

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
        clientele = Clientele.objects.create(last_name="Adekunle", first_name="Michael", clientele_id=0000,
                                             sex="Male", phone_no="09036451726", email="lekan@...", role="Admin")
        user = User.objects.create_user(username="0000", email=clientele.email,
                                        last_name=clientele.last_name, first_name=clientele.first_name,
                                        password=clientele.last_name)
        user.save()
        clientele.user = user
        clientele.save()
        comment = Comment.objects.create(clientele=clientele, comment='An article for your blog', date=timezone.now())

        blog = Blog.objects.create(title='Blog', article='An article for your blog', date=timezone.now(),
                                   image='Library/static/images/du logo.png')

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