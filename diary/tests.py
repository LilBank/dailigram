from django.test import TestCase , TransactionTestCase
from django.urls import reverse 
from .models import Page,Diary

class IndexTestCase(TestCase):
    def test_diary_exist(self):
        response = self.client.get(reverse('diary:index'))
        self.assertEqual(response.status_code, 200)

class TestsThatDependsOnPrimaryKeySequences(TransactionTestCase):
    reset_sequences = True

    def test_page_pk(self):
        page = Page.objects.create(story = "advanture")
        diary = Diary.objects.create(first_name = "tintin")
        self.assertEqual(page.pk + diary.pk, 2)
        





