from django.test import TestCase
from django import forms
from diary.forms import UserForm, PageForm
from diary.models import Page, Diary, Tag
from django.contrib.auth import get_user_model

class TestingForms(TestCase):

    def setUp(self):
         self.diary = Diary.objects.create(username='user')

    def test_valid_user_forms(self):
        """
        Test the valid user form data.
        """

        form = UserForm(
            data={'username': "user", 'password': "user", 'email': "user@gmail.com"})
        self.assertTrue(form.is_valid())

    def test_invalid_user_forms(self):
        """
        Test the invalid user form data. 
        """

        form = UserForm(
            data={'username': "", 'password': "", 'email': "", 'first_name': ""})
        self.assertFalse(form.is_valid())
    
    


    
