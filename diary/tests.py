from django.test import TestCase , TransactionTestCase
from django.urls import reverse 
from diary.models import Page,Diary
from django.db import connection
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
import time

class TestingModels(TestCase):

    def test_string_representation(self):
        """
        Test the string representation
        """
        page = Page(diary = 'tony')
        self.assertEqual(str(page), page.diary)

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
        num_pages = Page.objects.all().count()
        self.assertEqual(num_pages,0)

class TestingViews(TestCase):
    def test_setup(self):
        """
        Test diary existance by the response status code.
        """
        response = self.client.get(reverse('diary:index'))
        self.assertEqual(response.status_code, 200)

class TestingForms(TestCase):
    def test_setup1(self):
        """
        Test 
        """

class TestingAPI(TestCase):
    def test_setup2(self):
        """
        Test 
        """

class Command(BaseCommand):
    """Django command that waits for database to be available"""

    def handle(self, *args, **options):
        """Handle the command"""
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                connection.ensure_connection()
                db_conn = True
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
    

    

    
        





