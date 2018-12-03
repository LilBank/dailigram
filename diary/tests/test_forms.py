from django.test import TestCase
from django import forms
from diary.models import Page, Diary, Tag
from django.contrib.auth import get_user_model
from diary.forms import *

class TestingForms(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create(username="user", password="user", email="user@gmail.com" )


    def test_valid_user_forms(self):
        """
        Test the valid user form data.
        """

        form = UserForm(
            data={'username': "username", 'password': "user", 'email': "user@gmail.com"})
        self.assertTrue(form.is_valid())

    def test_invalid_user_forms(self):
        """
        Test the invalid user form data. 
        """

        form = UserForm(
            data={'username': "", 'password': "", 'email': "", 'first_name': ""})
        self.assertFalse(form.is_valid())
    
    def test_duplicate_user_forms(self):
        """
        Test the duplicate user form data. 
        """

        form = UserForm(
            data={'username': "user", 'password': "user", 'email': "user@gmail.com"})
        self.assertFalse(form.is_valid())
        
    def no_test_valid_page_forms(self):
        """
        Test the valid user form data.
        """

        form = PageForm(
            data={'title': "title", 'story': "short", 'tag': "happy"})
        self.full_clean()
        self.assertTrue(form.is_valid())

    


    
    


    
