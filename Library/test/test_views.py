from http import HTTPStatus

from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse
from django.utils import timezone

from Blog.models import Blog
from Library.forms import BlogForm, EbookForm
from Library.models import Clientele, Password, Journal


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
            Blog.objects.create(title=f'Blog{i + 1}', article='An article for your blog', date=timezone.now(),
                                image='Library/static/images/du logo.png')

    def test_url_exist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_is_accessible_by_name(self):
        response = self.client.get(reverse('Library:home'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_uses_correct_template(self):
        response = self.client.get(reverse('Library:home'))
        self.assertTemplateUsed(response, 'library/library_home.html')


class AboutViewTest(TestCase):

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

    def test_url_exist(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_is_accessible_by_name(self):
        response = self.client.get(reverse('Library:about'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_uses_correct_template(self):
        response = self.client.get(reverse('Library:about'))
        self.assertTemplateUsed(response, 'library/about.html')


class ContactViewTest(TestCase):

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

    def test_url_exist(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_is_accessible_by_name(self):
        response = self.client.get(reverse('Library:contact'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_uses_correct_template(self):
        response = self.client.get(reverse('Library:contact'))
        self.assertTemplateUsed(response, 'library/contact.html')


class LoginViewTest(TestCase):

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

        cls.data = {'user_id': '0000', 'password': 'Adekunle'}
        cls.fail_data = {'user_id': 'faildata', 'password': 'F41LD454'}

    def test_url_exist(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_is_accessible_by_name(self):
        response = self.client.get(reverse('Library:login'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_uses_correct_template(self):
        response = self.client.get(reverse('Library:login'))
        self.assertTemplateUsed(response, 'library/login.html')

    def test_user_is_logged_in(self):
        logged_in = self.client.login(username='0000', password='Adekunle')
        self.assertTrue(logged_in)

    def test_user_is_not_logged_in_with_fail_data(self):
        logged_in = self.client.login(username='fail', password='fail')
        self.assertFalse(logged_in)

    def test_url_exists_after_login_with_correct_data(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get(reverse('Library:login'))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_redirects_after_login_with_correct_data(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get(reverse('Library:login'))
        self.assertRedirects(response, reverse('Library:repository'))

    def test_url_still_works_after_login_with_fail_data(self):
        self.client.login(username='fail', password='fail')
        response = self.client.get(reverse('Library:login'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_exists_when_not_logged_in_with_correct_data(self):
        response = self.client.post(reverse('Library:login'), data=self.data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_exists_when_not_logged_in_with_fail_data(self):
        response = self.client.post(reverse('Library:login'), data=self.fail_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_redirects_when_not_logged_in_with_correct_data(self):
        response = self.client.post(reverse('Library:login'), data=self.data)
        self.assertRedirects(response, reverse('Library:repository'))

    def test_url_redirects_when_not_logged_in_with_fail_data(self):
        response = self.client.post(reverse('Library:login'), data=self.fail_data)
        self.assertRedirects(response, reverse('Library:login'))


class ForgottenPasswordViewTest(TestCase):

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

        Password.objects.create(clientele=cls.clientele, recovery_password='recovery_password', time=timezone.now())

        cls.data = {'user_id': '0000', 'email': 'lekan@...'}
        cls.fail_data = {'user_id': '', 'email': ''}

    def test_url_exist(self):
        response = self.client.get('/login/forgot-password/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_is_accessible_by_name(self):
        response = self.client.get(reverse('Library:forgot_password'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_uses_correct_template(self):
        response = self.client.get(reverse('Library:forgot_password'))
        self.assertTemplateUsed(response, 'library/forgot_password.html')

    def test_user_is_logged_in(self):
        logged_in = self.client.login(username='0000', password='Adekunle')
        self.assertTrue(logged_in)

    def test_user_is_not_logged_in_with_fail_data(self):
        logged_in = self.client.login(username='fail', password='fail')
        self.assertFalse(logged_in)

    def test_url_exists_after_login_with_correct_data(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get(reverse('Library:forgot_password'))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_redirects_after_login_with_correct_data(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get(reverse('Library:forgot_password'))
        self.assertRedirects(response, reverse('Library:repository'))

    def test_url_still_works_after_login_with_fail_data(self):
        self.client.login(username='fail', password='fail')
        response = self.client.post(reverse('Library:forgot_password'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_exists_when_not_logged_in_with_correct_data(self):
        response = self.client.post(reverse('Library:forgot_password'), data=self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_exists_when_not_logged_in_with_fail_data(self):
        response = self.client.post(reverse('Library:forgot_password'), data=self.fail_data)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class PasswordRetrievalViewTest(TestCase):

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

        cls.data = {'password': 'recovery_password'}
        cls.fail_data = {'password': 'faildata'}

    def test_url_exist(self):
        response = self.client.get(f'/login/forgot-password/{self.clientele.id}/retrieve-password/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_is_accessible_by_name(self):
        response = self.client.get(reverse('Library:password_retrieval', args=(self.clientele.id,)))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_uses_correct_template(self):
        response = self.client.get(reverse('Library:password_retrieval', args=(self.clientele.id,)))
        self.assertTemplateUsed(response, 'library/password_retrieval.html')

    def test_user_is_logged_in(self):
        logged_in = self.client.login(username='0000', password='Adekunle')
        self.assertTrue(logged_in)

    def test_user_is_not_logged_in_with_fail_data(self):
        logged_in = self.client.login(username='fail', password='fail')
        self.assertFalse(logged_in)

    def test_url_exists_after_login_with_correct_data(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get(reverse('Library:password_retrieval', args=(self.clientele.id,)))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_redirects_after_login_with_correct_data(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get(reverse('Library:password_retrieval', args=(self.clientele.id,)))
        self.assertRedirects(response, reverse('Library:repository'))

    def test_url_still_works_after_login_with_fail_data(self):
        self.client.login(username='fail', password='fail')
        response = self.client.post(reverse('Library:password_retrieval', args=(self.clientele.id,)))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_exists_when_not_logged_in_with_correct_data(self):
        self.client.login(username='fail', password='fail')
        response = self.client.post(reverse('Library:password_retrieval', args=(self.clientele.id,)), data=self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_exists_when_not_logged_in_with_fail_data(self):
        self.client.login(username='fail', password='fail')
        response = self.client.post(reverse('Library:password_retrieval', args=(self.clientele.id,)),
                                    data=self.fail_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_redirects_when_not_logged_in_with_fail_data(self):
        self.client.login(username='fail', password='fail')
        response = self.client.post(reverse('Library:password_retrieval', args=(self.clientele.id,)),
                                    data=self.fail_data)
        self.assertRedirects(response, reverse('Library:password_retrieval', args=(self.clientele.id,)))


class UpdatePasswordViewTest(TestCase):

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

        cls.data = {'password': 'password', 'confirm_password': 'password'}
        cls.fail_data = {'password': 'failure8', 'confirm_password': 'failureee'}

    def test_url_exist(self):
        response = self.client.get(f'/account/{self.clientele.id}/retrieve-password/update-password/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_is_accessible_by_name(self):
        response = self.client.get(reverse('Library:update_password', args=(self.clientele.id,)))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_uses_correct_template(self):
        response = self.client.get(reverse('Library:update_password', args=(self.clientele.id,)))
        self.assertTemplateUsed(response, 'library/update_password.html')

    def test_user_is_logged_in(self):
        logged_in = self.client.login(username='0000', password='Adekunle')
        self.assertTrue(logged_in)

    def test_user_is_not_logged_in_with_fail_data(self):
        logged_in = self.client.login(username='fail', password='fail')
        self.assertFalse(logged_in)

    def test_url_exists_after_login_with_correct_data(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get(reverse('Library:update_password', args=(self.clientele.id,)))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_still_works_after_login_with_fail_data(self):
        self.client.login(username='fail', password='fail')
        response = self.client.post(reverse('Library:update_password', args=(self.clientele.id,)))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_exists_with_correct_data(self):
        response = self.client.post(reverse('Library:update_password', args=(self.clientele.id,)), data=self.data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_exists_with_fail_data(self):
        response = self.client.post(reverse('Library:update_password', args=(self.clientele.id,)), data=self.fail_data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_redirects_when_not_logged_in_with_correct_data(self):
        response = self.client.post(reverse('Library:update_password', args=(self.clientele.id,)), data=self.data)
        self.assertRedirects(response, reverse('Library:login'))

    def test_url_redirects_when_not_logged_in_with_fail_data(self):
        response = self.client.post(reverse('Library:update_password', args=(self.clientele.id,)), data=self.fail_data)
        self.assertRedirects(response, reverse('Library:update_password', args=(self.clientele.id,)))


class RegisterViewTest(TestCase):

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

        cls.fail_data = {'last_name': "Adekunle", 'first_name': "Michael", 'user_id': '0000',
                         'sex': "Male", 'phone_no': "09036451726", 'email': "lekan@...", 'role': "Admin"}
        cls.data = {'last_name': "Maxwell", 'first_name': "Oladele", 'user_id': '2002',
                    'sex': "Male", 'phone_no': "09036455786", 'email': "maxwell@...", 'role': "Staff"}

    def test_url_exist(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_is_accessible_by_name(self):
        response = self.client.get(reverse('Library:register'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_uses_correct_template(self):
        response = self.client.get(reverse('Library:register'))
        self.assertTemplateUsed(response, 'library/signup.html')

    def test_user_is_logged_in(self):
        logged_in = self.client.login(username='0000', password='Adekunle')
        self.assertTrue(logged_in)

    def test_user_is_not_logged_in_with_fail_data(self):
        logged_in = self.client.login(username='fail', password='fail')
        self.assertFalse(logged_in)

    def test_url_exists_after_login_with_correct_data(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get(reverse('Library:register'))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_redirects_after_login_with_correct_data(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get(reverse('Library:register'))
        self.assertRedirects(response, reverse('Library:repository'))

    def test_url_still_works_after_login_with_fail_data(self):
        self.client.login(username='fail', password='fail')
        response = self.client.post(reverse('Library:register'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_exists_when_not_logged_in_with_correct_data(self):
        response = self.client.post(reverse('Library:register'), data=self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_exists_when_not_logged_in_with_fail_data(self):
        response = self.client.post(reverse('Library:register'), data=self.fail_data)
        self.assertEqual(response.status_code, HTTPStatus.OK)


class UpdateProfileImageViewTest(TestCase):

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

        cls.data = {'file': 'Library/static/books/COMPTIA-Roadmap.pdf'}

    def test_url_exist_without_login(self):
        response = self.client.get('/account/update-profile-image')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_is_accessible_by_name_without_login(self):
        response = self.client.get(reverse('Library:update_profile_image'))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_redirects_without_login(self):
        response = self.client.get(reverse('Library:update_profile_image'))
        self.assertRedirects(response, reverse('Library:login'))

    def test_url_exist(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get('/account/update-profile-image')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_is_accessible_by_name(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get(reverse('Library:update_profile_image'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_uses_correct_template(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.post(reverse('Library:update_profile_image'))
        self.assertTemplateUsed(response, 'library/update_profile_image.html')

    def test_user_is_logged_in(self):
        logged_in = self.client.login(username='0000', password='Adekunle')
        self.assertTrue(logged_in)

    def test_user_is_not_logged_in_with_fail_data(self):
        logged_in = self.client.login(username='fail', password='fail')
        self.assertFalse(logged_in)

    def test_url_exists_after_login_with_correct_data(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get(reverse('Library:update_profile_image'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_still_works_after_login_with_fail_data(self):
        self.client.login(username='fail', password='fail')
        response = self.client.post(reverse('Library:update_profile_image'))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_exists_when_not_logged_in_with_correct_data(self):
        response = self.client.post(reverse('Library:update_profile_image'), data=self.data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_redirects_when_not_logged_in(self):
        response = self.client.post(reverse('Library:update_profile_image'))
        self.assertRedirects(response, reverse('Library:login'))

    def test_url_redirects_when_not_logged_in_with_correct_data(self):
        response = self.client.post(reverse('Library:update_profile_image'), data=self.data)
        self.assertRedirects(response, reverse('Library:login'))


class RepositoryViewTest(TestCase):

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

    def test_url_exist_without_login(self):
        response = self.client.get('/account/repository')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_is_accessible_by_name_without_login(self):
        response = self.client.get(reverse('Library:repository'))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_redirects_without_login(self):
        response = self.client.get(reverse('Library:repository'))
        self.assertRedirects(response, reverse('Library:login'))

    def test_url_exist(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get('/account/repository')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_is_accessible_by_name(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get(reverse('Library:repository'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_uses_correct_template(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get(reverse('Library:repository'))
        self.assertTemplateUsed(response, 'library/library_main.html')

    def test_user_is_logged_in(self):
        logged_in = self.client.login(username='0000', password='Adekunle')
        self.assertTrue(logged_in)

    def test_user_is_not_logged_in_with_fail_data(self):
        logged_in = self.client.login(username='fail', password='fail')
        self.assertFalse(logged_in)

    def test_url_still_works_after_login_with_fail_data(self):
        self.client.login(username='fail', password='fail')
        response = self.client.post(reverse('Library:repository'))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)


class OfflineResourcesViewTest(TestCase):

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

    def test_url_exist_without_login(self):
        response = self.client.get('/account/repository/e-books')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_is_accessible_by_name_without_login(self):
        response = self.client.get(reverse('Library:offline_resources'))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_redirects_without_login(self):
        response = self.client.get(reverse('Library:offline_resources'))
        self.assertRedirects(response, reverse('Library:login'))

    def test_url_exist(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get('/account/repository/e-books')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_is_accessible_by_name(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get(reverse('Library:offline_resources'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_uses_correct_template(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get(reverse('Library:offline_resources'))
        self.assertTemplateUsed(response, 'library/offline_resources.html')

    def test_user_is_logged_in(self):
        logged_in = self.client.login(username='0000', password='Adekunle')
        self.assertTrue(logged_in)

    def test_user_is_not_logged_in_with_fail_data(self):
        logged_in = self.client.login(username='fail', password='fail')
        self.assertFalse(logged_in)

    def test_url_still_works_after_login_with_fail_data(self):
        self.client.login(username='fail', password='fail')
        response = self.client.post(reverse('Library:offline_resources'))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)


class LibraryAdminViewTest(TestCase):

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

        group = Group.objects.get(name='Admin')
        group.user_set.add(user)

        cls.clientele2 = Clientele.objects.create(last_name="Adekunle1", first_name="Michael1", clientele_id='0001',
                                                 sex="Male", phone_no="09036451726", email="lekan@...", role="Student")
        user2 = User.objects.create_user(username="0001", email=cls.clientele2.email,
                                        last_name=cls.clientele2.last_name, first_name=cls.clientele2.first_name,
                                        password=cls.clientele2.last_name)
        user2.save()
        cls.clientele2.user = user2
        cls.clientele2.save()

        group2 = Group.objects.get(name='Student')
        group2.user_set.add(user2)

        for i in range(5):
            Journal.objects.create(title=f'Journal{i+1}', authors=f'authors{i+1}', description=f'description{i+1}',
                                   date=timezone.now(), file='Library/static/books/COMPTIA-Roadmap.pdf')
            Blog.objects.create(title=f'Blog{i+1}', article=f'{i+1}: An article for your blog', date=timezone.now(),
                                image='Library/static/images/du logo.png')
            Clientele.objects.create(last_name=f"Adekunle{i+2}", first_name=f"Michael{i+2}", clientele_id=f'000{i+2}',
                                     sex="Male", phone_no=f"090{i+1}64{i+3}1726", email=f"lekan{i+1}@...", role="Student")

        cls.ebook = {'title': 'title', 'authors': 'authors', 'description': 'description', 'programme': 'programme',
                     'file': 'Library/static/books/COMPTIA-Roadmap.pdf'}
        cls.journal = {'title': 'title', 'authors': 'authors', 'description': 'description',
                       'file': 'Library/static/books/COMPTIA-Roadmap.pdf'}
        cls.blog = {'title': 'title', 'authors': 'article', 'article': 'description',
                    'image': 'Library/static/images/flake.png'}

    def test_url_exist_without_login(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_is_accessible_by_name_without_login(self):
        response = self.client.get(reverse('Library:library_admin'))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_redirects_without_login(self):
        response = self.client.get(reverse('Library:library_admin'))
        self.assertRedirects(response, reverse('Library:login'))

    def test_url_exist_if_student_with_login(self):
        self.client.login(username='0001', password='Adekunle1')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_is_accessible_by_name_if_student_with_login(self):
        self.client.login(username='0001', password='Adekunle1')
        response = self.client.get(reverse('Library:library_admin'))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_redirects_if_student_with_login(self):
        self.client.login(username='0001', password='Adekunle1')
        response = self.client.get(reverse('Library:library_admin'))
        self.assertRedirects(response, reverse('Library:home'))

    def test_url_exist(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_is_accessible_by_name(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get(reverse('Library:library_admin'))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_uses_correct_template(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.get(reverse('Library:library_admin'))
        self.assertTemplateUsed(response, 'library/library_admin.html')

    def test_user_is_logged_in(self):
        logged_in = self.client.login(username='0000', password='Adekunle')
        self.assertTrue(logged_in)

    def test_user_is_not_logged_in_with_fail_data(self):
        logged_in = self.client.login(username='fail', password='fail')
        self.assertFalse(logged_in)

    def test_url_still_works_after_login_with_fail_data(self):
        self.client.login(username='fail', password='fail')
        response = self.client.post(reverse('Library:library_admin'))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)


class ApproveClieneteleViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Group.objects.create(name='Admin')
        Group.objects.create(name='Student')

        cls.clientele = Clientele.objects.create(last_name="Adekunle", first_name="Michael", clientele_id='0000',
                                                 sex="Male", phone_no="09036451726", email="lekan@...", role="Student")

    def test_url_exist(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.post(f'/admin/approve-clientele/{self.clientele.id}')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_is_accessible_by_name(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.post(reverse('Library:approve_clientele', args=(self.clientele.id,)))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)


class RejectClieneteleViewTest(TestCase):

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

        group = Group.objects.get(name='Admin')
        group.user_set.add(user)

    def test_url_exist(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.post(f'/admin/reject-clientele/{self.clientele.id}')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_is_accessible_by_name(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.post(reverse('Library:reject_clientele', args=(self.clientele.id,)))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)


class ApproveJournalViewTest(TestCase):

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

        group = Group.objects.get(name='Admin')
        group.user_set.add(user)
        cls.journal = Journal.objects.create(title='Journal', authors='authors', description='description',
                                             date=timezone.now(), file='Library/static/books/COMPTIA-Roadmap.pdf')

    def test_url_exist(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.post(f'/admin/approve-journal/{self.journal.id}')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_is_accessible_by_name(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.post(reverse('Library:approve_journal', args=(self.journal.id,)))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)


class RejectJournalViewTest(TestCase):

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

        group = Group.objects.get(name='Admin')
        group.user_set.add(user)
        cls.journal = Journal.objects.create(title='Journal', authors='authors', description='description',
                                             date=timezone.now(), file='Library/static/books/COMPTIA-Roadmap.pdf')

    def test_url_exist(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.post(f'/admin/reject-journal/{self.journal.id}')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_is_accessible_by_name(self):
        self.client.login(username='0000', password='Adekunle')
        response = self.client.post(reverse('Library:reject_journal', args=(self.journal.id,)))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)


class LogoutViewTest(SimpleTestCase):

    def test_url_exist(self):
        response = self.client.post(f'/account/logout')
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_is_accessible_by_name(self):
        response = self.client.post(reverse('Library:logout'))
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_url_redirects(self):
        response = self.client.post(reverse('Library:logout'))
        self.assertRedirects(response, reverse('Library:login'))


class Error404ViewTest(SimpleTestCase):

    def test_url_exist(self):
        response = self.client.post(f'/jdhdhjkf')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_redirects(self):
        response = self.client.post('/jdhdhjkf')
        self.assertTemplateUsed(response, 'library/404.html')
