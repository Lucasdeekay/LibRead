from django.test import TestCase

from http import HTTPStatus

from rest_framework.test import APITestCase


class ClienteleSerializerTest(APITestCase):

    def test_clientele_api_url_exists(self):
        response = self.client.get('/api/clientele/')
        self.assertEqual(response.status_code, HTTPStatus.OK)


class PasswordSerializerTest(APITestCase):

    def test_password_api_url_exists(self):
        response = self.client.get('/api/password/')
        self.assertEqual(response.status_code, HTTPStatus.OK)


class EbookSerializerTest(APITestCase):

    def test_ebook_api_url_exists(self):
        response = self.client.get('/api/ebook/')
        self.assertEqual(response.status_code, HTTPStatus.OK)


class JournalSerializerTest(APITestCase):

    def test_journal_api_url_exists(self):
        response = self.client.get('/api/journal/')
        self.assertEqual(response.status_code, HTTPStatus.OK)


class LibraryFileSerializerTest(APITestCase):

    def test_ebook_api_url_exists(self):
        response = self.client.get('/api/library-file/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
