from http import HTTPStatus

from rest_framework.test import APITestCase


class BlogSerializerTest(APITestCase):

    def test_blog_api_url_exists(self):
        response = self.client.get('/blog/api/blog/')
        self.assertEqual(response.status_code, HTTPStatus.OK)