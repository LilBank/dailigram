from django.test import TestCase , TransactionTestCase
from django.urls import reverse 
from diary.models import Page,Diary

class IndexTestCase(TestCase):
    def test_setup(self):
        """
        Test diary existance by the response status code.
        """
        response = self.client.get(reverse('diary:index'))
        self.assertEqual(response.status_code, 200)
    def test_all_objects(self):
        """
        Test 
        """
        num_pages = Page.objects.all().count()
        self.assertEqual(num_pages,0)

    

class PrimaryKeyTestCase(TransactionTestCase):
    reset_sequences = True

    def test_page_pk(self):
        """
        The primary key should be one for each object's creation. 
        """
        page = Page.objects.create(story = "advanture")
        diary = Diary.objects.create(first_name = "tintin")
        self.assertEqual(page.pk + diary.pk, 2)
        





