from http import HTTPStatus

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from Blog.models import Blog
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
