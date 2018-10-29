from django.test import TestCase 
from django.urls import reverse
from diary.models import Page,Diary
from django import forms

class TestingModels(TestCase):

    def test_diary_pk(self):
        """
        Test that the primary key should be one for each object's creation. 
        """
        diary = Diary.objects.create(first_name = 'tintin')
        self.assertEqual(diary.pk ,1)

    def test_string_representation(self):
        """
        Test that the string is correctly represented.
        """
        diary = Diary(first_name = 'tony')
        self.assertEqual(str(diary), diary.first_name)

    def test_diary_max_length(self):
        """
        Test that the max length of the field is equal or not.
        """
        diary = Diary(first_name = 'tony')
        max_length = diary._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_no_diary_by_model(self):
        """
        Test that the total number of object is 0 when nothing is created.
        """
        num_diary = Diary.objects.all().count()
        self.assertEqual(num_diary,0)

    def test_get_absolute_url(self):
        """
        Test that the getting absolute url is correct.
        """
        diary = Diary(first_name = 'tony')
        self.assertEquals(diary.get_absolute_url(), '/diary/user/1')

class TestingViews(TestCase):

    def test_connection(self):
        """
        Test diary's existance by the response status code.
        """
        response = self.client.get(reverse('diary:index'))
        self.assertEqual(response.status_code, 200)

    def test_no_diary_by_view(self):
        """
        Test that the co
        """
        response = self.client.get(reverse('diary:index'))
        self.assertQuerysetEqual(response.context['all_diarys'], [])



    

    
        





