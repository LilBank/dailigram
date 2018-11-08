from django.test import TestCase
from django.urls import reverse
from diary.models import Page, Diary, Tag
from django import forms
from diary.forms import UserForm
from .forms import *
from selenium import webdriver


class TestingModels(TestCase):

    def setUp(self):
        """
        Set up creating database's objects
        """
        Diary.objects.create(first_name='tony')
        Diary.objects.create(first_name='tintin')
        diary = Diary.objects.all()

        Tag.objects.create(name='happy')
        Tag.objects.create(name='sad')
        tag = Tag.objects.all()

        Page.objects.create(
            diary=diary[0], tag=tag[0], story='This was awesome', date='2018-11-06', picture='pic1')
        Page.objects.create(
            diary=diary[1], tag=tag[1], story='This was awesome', date='2018-11-06', picture='pic1')

    def test_count_diary(self):
        """
        Test counting the total diarys.
        """
        num_diary = Diary.objects.all().count()
        self.assertEqual(num_diary, 2)

    def test_count_tag(self):
        """
        Test counting the total tags.
        """
        num_tag = Tag.objects.all().count()
        self.assertEqual(num_tag, 2)

    def test_count_page(self):
        """
        Test counting the total pages.
        """
        num_page = Page.objects.all().count()
        self.assertEqual(num_page, 2)

    def test_diary_first_name(self):
        """
        Test the diary object's first name.
        """
        diary = Diary.objects.all()
        self.assertEqual(diary[0].first_name, 'tony')
        self.assertEqual(diary[1].first_name, 'tintin')

    def test_tag_name(self):
        """
        Test the tag object' name.
        """
        tag = Tag.objects.all()
        self.assertEqual(tag[0].name, 'happy')
        self.assertEqual(tag[1].name, 'sad')

    def test_diary_string_representation(self):
        """
        Test that the string is correctly represented in diary.
        """
        diary = Diary.objects.all()
        self.assertEqual(str(diary[0]), diary[0].first_name)
        self.assertEqual(str(diary[1]), diary[1].first_name)

    def test_tag_string_representation(self):
        """
        Test that the string is correctly represented in diary's tag.
        """
        tag = Tag.objects.all()
        self.assertEqual(str(tag[0]), tag[0].name)
        self.assertEqual(str(tag[1]), tag[1].name)

    def test_diary_max_length(self):
        """
        Test that the max length of the field is equal or not.
        """
        diary = Diary(first_name='tony')
        max_length = diary._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_get_absolute_url(self):
        page = Page.objects.all()
        self.assertEquals(page[0].get_absolute_url(), '/diary/')


class TestingViews(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'user',
            'password': 'user'}
        User.objects.create_user(**self.credentials)

    def test_accessible_by_name(self):
        """
        Test diary's accessible by name.
        """
        response = self.client.get(reverse('diary:login'))
        self.assertEqual(response.status_code, 200)

    def test_accessible_by_location(self):
        """
        Test diary's accessible by location.
        """
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_no_diary_by_view(self):
        """
        Test that the total context object is 0 when nothing is inserted.
        """
        response = self.client.get(reverse('diary:login'))
        self.assertQuerysetEqual(response.context['all_diarys'], [])

    def test_user_authenticated(self):
        """
        Test if the login is sucess or not
        """
        response = self.client.post(
            '/accounts/login/', **self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)


class TestingForms(TestCase):

    def setUp(self):
        """
        Setup the creation of user.
        """
        self.user = User.objects.create(
            username="user", password="user", email="user@gmail.com")

    def test_valid_user_forms(self):
        """
        Test the valid form data 
        """
        form = UserForm()
        self.assertTrue(form.is_valid())

    def test_invalid_user_forms(self):
        """
        Test the invalid form data 
        """
        form = UserForm(
            data={'username': "", 'password': "", 'email': "", 'first_name': ""})
        self.assertFalse(form.is_valid())


# class TestingWeb():
#     chromedriver = "/staticfiles"
#     driver = webdriver.Chrome(chromedriver)
#     driver.get
