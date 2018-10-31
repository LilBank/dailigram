from django.test import TestCase
from django.urls import reverse
from diary.models import Page, Diary
from django import forms
from diary.forms import UserForm
from util import GCloudUtil


class TestingModels(TestCase):

    def test_diary_pk(self):
        """
        Test that the primary key should be one for each object's creation.
        """
        diary = Diary.objects.create(first_name='tintin')
        self.assertEqual(diary.pk, 1)

    def test_string_representation(self):
        """
        Test that the string is correctly represented.
        """
        diary = Diary.objects.create(first_name='tintin')
        self.assertEqual(str(diary), diary.first_name)

    def test_diary_max_length(self):
        """
        Test that the max length of the field is equal or not.
        """
        diary = Diary(first_name='tony')
        max_length = diary._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_no_diary_by_model(self):
        """
        Test that the total number of object is 0 when nothing is created.
        """
        num_diary = Diary.objects.all().count()
        self.assertEqual(num_diary, 0)


class TestingViews(TestCase):

    def test_connection(self):
        """
        Test diary's existance by the response status code.
        """
        response = self.client.get(reverse('diary:index'))
        self.assertEqual(response.status_code, 200)

    def test_no_diary_by_view(self):
        """
        Test that the total context object is 0 when nothing is inserted.
        """
        response = self.client.get(reverse('diary:index'))
        self.assertQuerysetEqual(response.context['all_diarys'], [])


class TestingForms(TestCase):

    def test_valid_forms(self):
        """
        Test if the form is valid or not.
        """
        form = UserForm()
        self.assertTrue(form.is_valid)


class GcloudTest(TestCase):

    bucket_name = 'testBucket'
    GCloudUtil.create_bucket(bucket_name)

    def test_simple_upload(self):
        """
        Test if single upload success.
        """
        local_file1 = open("test1.txt","x")
        text = "Hello World!"
        local_file1.write(text)
        GCloudUtil.upload(bucket_name,"test1.txt")
        file1_text = GCloudUtil.blob_metadata
        self.assertEqual(text,file1_text)


#     def test_multiple_upload(self):
#         """
#         Test if multiple upload success.
#         """

#     def test_get_list_blobs(self):
#         """
#         Test retrieving blobs.
#         """

#    def test_get_long_list(self)
#         """
#         Test retrieving lots of blobs.
#         """

#     def test_delete_blob(self)
#         """
#         Test deleting a blob
#         """

