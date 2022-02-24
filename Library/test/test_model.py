from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.utils import timezone

from Library.models import Clientele, Password, Ebook, Journal, LibraryFile


class ClienteleModelTest(TestCase):

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

    def test_user_label(self):
        clientele = get_object_or_404(Clientele, last_name="Adekunle")
        field_label = clientele._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_last_name_label(self):
        clientele = get_object_or_404(Clientele, last_name="Adekunle")
        field_label = clientele._meta.get_field('last_name').verbose_name
        self.assertEqual(field_label, 'last name')

    def test_last_name_max_length(self):
        clientele = get_object_or_404(Clientele, last_name="Adekunle")
        max_length = clientele._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 50)

    def test_first_name_label(self):
        clientele = get_object_or_404(Clientele, last_name="Adekunle")
        field_label = clientele._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_first_name_max_length(self):
        clientele = get_object_or_404(Clientele, last_name="Adekunle")
        max_length = clientele._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 50)

    def test_clientele_id_label(self):
        clientele = get_object_or_404(Clientele, last_name="Adekunle")
        field_label = clientele._meta.get_field('clientele_id').verbose_name
        self.assertEqual(field_label, 'clientele id')

    def test_clientele_id_max_length(self):
        clientele = get_object_or_404(Clientele, last_name="Adekunle")
        max_length = clientele._meta.get_field('clientele_id').max_length
        self.assertEqual(max_length, 30)

    def test_sex_label(self):
        clientele = get_object_or_404(Clientele, last_name="Adekunle")
        field_label = clientele._meta.get_field('sex').verbose_name
        self.assertEqual(field_label, 'sex')

    def test_sex_max_length(self):
        clientele = get_object_or_404(Clientele, last_name="Adekunle")
        max_length = clientele._meta.get_field('sex').max_length
        self.assertEqual(max_length, 10)

    def test_phone_no_label(self):
        clientele = get_object_or_404(Clientele, last_name="Adekunle")
        field_label = clientele._meta.get_field('phone_no').verbose_name
        self.assertEqual(field_label, 'phone no')

    def test_phone_no_max_length(self):
        clientele = get_object_or_404(Clientele, last_name="Adekunle")
        max_length = clientele._meta.get_field('phone_no').max_length
        self.assertEqual(max_length, 20)

    def test_email_label(self):
        clientele = get_object_or_404(Clientele, last_name="Adekunle")
        field_label = clientele._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_role_label(self):
        clientele = get_object_or_404(Clientele, last_name="Adekunle")
        field_label = clientele._meta.get_field('role').verbose_name
        self.assertEqual(field_label, 'role')

    def test_role_max_length(self):
        clientele = get_object_or_404(Clientele, last_name="Adekunle")
        max_length = clientele._meta.get_field('role').max_length
        self.assertEqual(max_length, 10)

    def test_image_label(self):
        clientele = get_object_or_404(Clientele, last_name="Adekunle")
        field_label = clientele._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'image')

    def test_is_approved_label(self):
        clientele = get_object_or_404(Clientele, last_name="Adekunle")
        field_label = clientele._meta.get_field('is_approved').verbose_name
        self.assertEqual(field_label, 'is approved')


class PasswordModelTest(TestCase):

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
        Password.objects.create(clientele=clientele, recovery_password='recovery', time=timezone.now())

    def test_clientele_label(self):
        password = get_object_or_404(Password, recovery_password='recovery')
        field_label = password._meta.get_field('clientele').verbose_name
        self.assertEqual(field_label, 'clientele')

    def test_recovery_password_label(self):
        password = get_object_or_404(Password, recovery_password='recovery')
        field_label = password._meta.get_field('recovery_password').verbose_name
        self.assertEqual(field_label, 'recovery password')

    def test_recovery_password_max_length(self):
        password = get_object_or_404(Password, recovery_password='recovery')
        max_length = password._meta.get_field('recovery_password').max_length
        self.assertEqual(max_length, 12)

    def test_time_label(self):
        password = get_object_or_404(Password, recovery_password='recovery')
        field_label = password._meta.get_field('time').verbose_name
        self.assertEqual(field_label, 'time')


class EbookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Ebook.objects.create(title='Ebook', authors='authors', description='description',
                             date=timezone.now(), file='Library/static/books/COMPTIA-Roadmap.pdf')

    def test_title_label(self):
        ebook = get_object_or_404(Ebook, title='Ebook')
        field_label = ebook._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_max_length(self):
        ebook = get_object_or_404(Ebook, title='Ebook')
        max_length = ebook._meta.get_field('title').max_length
        self.assertEqual(max_length, 250)

    def test_authors_label(self):
        ebook = get_object_or_404(Ebook, title='Ebook')
        field_label = ebook._meta.get_field('authors').verbose_name
        self.assertEqual(field_label, 'authors')

    def test_authors_max_length(self):
        ebook = get_object_or_404(Ebook, title='Ebook')
        max_length = ebook._meta.get_field('authors').max_length
        self.assertEqual(max_length, 200)

    def test_description_label(self):
        ebook = get_object_or_404(Ebook, title='Ebook')
        field_label = ebook._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_description_max_length(self):
        ebook = get_object_or_404(Ebook, title='Ebook')
        max_length = ebook._meta.get_field('description').max_length
        self.assertEqual(max_length, 250)

    def test_date_label(self):
        ebook = get_object_or_404(Ebook, title='Ebook')
        field_label = ebook._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_file_label(self):
        ebook = get_object_or_404(Ebook, title='Ebook')
        field_label = ebook._meta.get_field('file').verbose_name
        self.assertEqual(field_label, 'file')


class JournalModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Journal.objects.create(title='Journal', authors='authors', description='description',
                             date=timezone.now(), file='Library/static/books/COMPTIA-Roadmap.pdf')

    def test_title_label(self):
        journal = get_object_or_404(Journal, title='Journal')
        field_label = journal._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_max_length(self):
        journal = get_object_or_404(Journal, title='Journal')
        max_length = journal._meta.get_field('title').max_length
        self.assertEqual(max_length, 250)

    def test_authors_label(self):
        journal = get_object_or_404(Journal, title='Journal')
        field_label = journal._meta.get_field('authors').verbose_name
        self.assertEqual(field_label, 'authors')

    def test_authors_max_length(self):
        journal = get_object_or_404(Journal, title='Journal')
        max_length = journal._meta.get_field('authors').max_length
        self.assertEqual(max_length, 200)

    def test_description_label(self):
        journal = get_object_or_404(Journal, title='Journal')
        field_label = journal._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_description_max_length(self):
        journal = get_object_or_404(Journal, title='Journal')
        max_length = journal._meta.get_field('description').max_length
        self.assertEqual(max_length, 250)

    def test_date_label(self):
        journal = get_object_or_404(Journal, title='Journal')
        field_label = journal._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_file_label(self):
        journal = get_object_or_404(Journal, title='Journal')
        field_label = journal._meta.get_field('file').verbose_name
        self.assertEqual(field_label, 'file')

    def test_is_approved_label(self):
        journal = get_object_or_404(Journal, title='Journal')
        field_label = journal._meta.get_field('is_approved').verbose_name
        self.assertEqual(field_label, 'is approved')


class LibraryFileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        ebook = Ebook.objects.create(title='Ebook', authors='authors', description='description',
                             date=timezone.now(), file='Library/static/books/COMPTIA-Roadmap.pdf')
        journal = Journal.objects.create(title='Journal', authors='authors', description='description',
                                         date=timezone.now(), file='Library/static/books/COMPTIA-Roadmap.pdf')
        library_file = LibraryFile.objects.create(programme='programme')
        library_file.ebook.add(ebook)
        library_file.journal.add(journal)

    def test_programme_label(self):
        library_file = get_object_or_404(LibraryFile, programme='programme')
        field_label = library_file._meta.get_field('programme').verbose_name
        self.assertEqual(field_label, 'programme')

    def test_programme_max_length(self):
        library_file = get_object_or_404(LibraryFile, programme='programme')
        max_length = library_file._meta.get_field('programme').max_length
        self.assertEqual(max_length, 250)

    def test_ebook_label(self):
        library_file = get_object_or_404(LibraryFile, programme='programme')
        field_label = library_file._meta.get_field('ebook').verbose_name
        self.assertEqual(field_label, 'ebook')

    def test_journal_label(self):
        library_file = get_object_or_404(LibraryFile, programme='programme')
        field_label = library_file._meta.get_field('journal').verbose_name
        self.assertEqual(field_label, 'journal')

