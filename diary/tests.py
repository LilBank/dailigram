from django.test import TestCase 
from django.urls import reverse
from diary.models import Page,Diary
from django import forms

class TestingModels(TestCase):

    def test_string_representation(self):
        """
        Test the string representation
        """
        diary = Diary(first_name = 'tony')
        self.assertEqual(str(diary), diary.first_name)

    def test_page_pk(self):
        """
        Test that the primary key should be one for each object's creation. 
        """
        diary = Diary.objects.create(first_name = 'tintin')
        self.assertEqual(diary.pk ,1)

    def test_all_objects(self):
        """
        Test the number of object in the list
        """
        num_diary = Diary.objects.all().count()
        self.assertEqual(num_diary,0)

class TestingViews(TestCase):

    def test_connection(self):
        """
        Test diary existance by the response status code.
        """
        response = self.client.get(reverse('diary:index'))
        self.assertEqual(response.status_code, 200)

    def test_no_diary(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('diary:index'))
        self.assertQuerysetEqual(response.context['all_diarys'], [])



    

    
        





