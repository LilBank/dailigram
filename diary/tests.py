from django.test import TestCase
from django.urls import reverse
from diary.models import Page, Diary
from django import forms
from diary.forms import UserForm
from utility.imgur import ImgurUtil


# class ModelTest(TestCase):

#     def test_diary_pk(self):
#         """
#         Test that the primary key should be one for each object's creation.
#         """
#         diary = Diary.objects.create(first_name='tintin')
#         self.assertEqual(diary.pk, 1)

#     def test_string_representation(self):
#         """
#         Test that the string is correctly represented.
#         """
#         diary = Diary.objects.create(first_name='tintin')
#         self.assertEqual(str(diary), diary.first_name)

#     def test_diary_max_length(self):
#         """
#         Test that the max length of the field is equal or not.
#         """
#         diary = Diary(first_name='tony')
#         max_length = diary._meta.get_field('first_name').max_length
#         self.assertEquals(max_length, 100)

#     def test_no_diary_by_model(self):
#         """
#         Test that the total number of object is 0 when nothing is created.
#         """
#         num_diary = Diary.objects.all().count()
#         self.assertEqual(num_diary, 0)


# class ViewTest(TestCase):

#     def test_connection(self):
#         """
#         Test diary's existance by the response status code.
#         """
#         response = self.client.get(reverse('diary:index'))
#         self.assertEqual(response.status_code, 200)

#     def test_no_diary_by_view(self):
#         """
#         Test that the total context object is 0 when nothing is inserted.
#         """
#         response = self.client.get(reverse('diary:index'))
#         self.assertQuerysetEqual(response.context['all_diarys'], [])


# class FormTest(TestCase):

#     def test_valid_forms(self):
#         """
#         Test if the form is valid or not.
#         """
#         form = UserForm()
#         self.assertTrue(form.is_valid)


class ImgurUtilTest(TestCase):

    def test_get_single_image(self):
        """
        Test getting an single image from test_album.
        """

        albumHash = 'z02PMYd'
        imageHash = 'DYU8bxj'
        imgurUtil = ImgurUtil()
        image_des = imgurUtil.get_image_description(albumHash, imageHash)
        description = 'Catterpillar'
        self.assertEqual(image_des, description)

    def test_get_multiple_image(self):
        """
        Test getting multiple image from test_album.
        """
        imgurUtil = ImgurUtil()
        albumHash = 'z02PMYd'

        image1_hash = 'DYU8bxj'
        image1_des = imgurUtil.get_image_description(albumHash, image1_hash)
        des1 = 'Catterpillar'

        image2_hash = 'vACxphT'
        image2_des = imgurUtil.get_image_description(albumHash, image2_hash)
        des2 = 'Sea and mountain'

        image3_hash = 'UkJdqD9'
        image3_des = imgurUtil.get_image_description(albumHash, image3_hash)
        des3 = 'Catty'

        self.assertEqual(image1_des, des1)
        self.assertEqual(image2_des, des2)
        self.assertEqual(image3_des, des3)

    def test_create_album(self):
        """
        Create a temporary album for testing.
        """
        imgurUtil = ImgurUtil()
        response = imgurUtil.create_album('temp_album')
        self.assertEqual(response.status_code, 200)

    def test_create_many_albums(self):
        """
        Create many albums for testing.
        """

        imgurUtil = ImgurUtil()
        response1 = imgurUtil.create_album('album1')
        response2 = imgurUtil.create_album('album2')
        response3 = imgurUtil.create_album('album3')
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)

    def test_get_all_albums(self):
        """
        Test get all album hashes for further use in the test.
        """
        
        imgurUtil = ImgurUtil()
        response = imgurUtil.get_all_albums_info()
        self.assertEqual(response['status'], 200)

    def test_single_upload(self):
        """
        Test if single upload success.
        """

        pass

    def test_multiple_upload(self):
        """
        Test if multiple upload success.
        """

        pass

    def test_delete_single_image(self):
        """
        Test deleting a picture.
        """

        pass

    def test_delete_multiple_image(self):
        """
        Test deleting many pictures.
        """

        pass

    def test_delete_album(self):
        """
        Test delete an album.
        """

        imgurUtil = ImgurUtil()
        albumTitle = 'temp_album'
        response = imgurUtil.delete_album(albumTitle)
        self.assertEqual(response['status'],200)

    def test_delete_multiple_albums(self):
        """
        Test delete many albums.
        """

        imgurUtil = ImgurUtil()
        albumTitle_1 = 'album1'
        albumTitle_2 = 'album2'
        albumTitle_3 = 'album3'
        response1 = imgurUtil.delete_album(albumTitle_1)
        response2 = imgurUtil.delete_album(albumTitle_2)
        response3 = imgurUtil.delete_album(albumTitle_3)
        self.assertEqual(response1['status'],200)
        self.assertEqual(response2['status'],200)
        self.assertEqual(response3['status'],200)

