from django.test import TestCase
from django.urls import reverse
from django.test.client import Client
from diary.forms import *


class TestingViews(TestCase):

    def setUp(self):
        """
        Set up the client and credentials.
        """

        self.client = Client()
        self.credentials = {
            'username': 'user',
            'password': 'user'}
        User.objects.create_user(**self.credentials)

    def test_accessible_by_name(self):
        """
        Test diary's accessible by name.
        """

        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_accessible_by_location(self):
        """
        Test diary's accessible by location.
        """

        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
    
    def test_using_correct_template(self):
        """
        Test that the login is using the correct template path.
        """
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_post_request(self):
        """
        Test the submission of post request.
        """

        response = self.client.post(
            '/login/', {'username': 'test', 'password': 'test'})
        self.assertEqual(response.status_code, 200)

    def test_user_authenticated(self):
        """
        Test if the login is sucess or not.
        """

        response = self.client.post(
            '/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
    
    
    
