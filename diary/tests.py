from django.test import TestCase
from django.urls import reverse
from diary.models import Page, Diary
from django import forms
from diary.forms import UserForm
from utility.imgur import ImgurUtil


class ModelTest(TestCase):

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


class FormTest(TestCase):

    def test_valid_forms(self):
        """
        Test if the form is valid or not.
        """
        form = UserForm()
        self.assertTrue(form.is_valid)


class ImgurUtilTest(TestCase):

    # def test_get_images(self):
    #     """
    #     Test retrieving all images from imgur homepage.
    #     """

    #     items = ImgurUtil.get_all_homepage_image()
    #     count = 0
    #     for item in items:
    #         count += 1

    #     self.assertTrue(count > 0)

    # def test_get_single_image(self):
    #     """
    #     Test getting an single image from test_album.
    #     """
    #     albumHash = 'z02PMYd'
    #     imageHash = 'DYU8bxj'
    #     ImgurUtil.set_albumHash('', albumHash)
    #     ImgurUtil.set_imageHash('', imageHash)
    #     image_des = ImgurUtil.get_image_description('')
    #     description = 'Catterpillar'
    #     self.assertEqual(image_des, description)

    # def test_get_multiple_image(self):
    #     """
    #     Test getting multiple image from test_album.
    #     """
    #     albumHash = 'z02PMYd'
    #     ImgurUtil.set_albumHash('', albumHash)

    #     image1_hash = 'DYU8bxj'
    #     ImgurUtil.set_imageHash('', image1_hash)
    #     image1_des = ImgurUtil.get_image_description('')
    #     des1 = 'Catterpillar'

    #     image2_hash = 'vACxphT'
    #     ImgurUtil.set_imageHash('', image2_hash)
    #     image2_des = ImgurUtil.get_image_description('')
    #     des2 = 'Sea and mountain'

    #     image3_hash = 'UkJdqD9'
    #     ImgurUtil.set_imageHash('', image3_hash)
    #     image3_des = ImgurUtil.get_image_description('')
    #     des3 = 'Catty'

    #     self.assertEqual(image1_des, des1)
    #     self.assertEqual(image2_des, des2)
    #     self.assertEqual(image3_des, des3)

    # def test_create_album(self):
    #     """
    #     Create a temporary album for testing.
    #     """

    #     response = ImgurUtil.create_album('','temp_album')
    #     self.assertEqual(response.status_code, 200)

    def test_get_all_albums(self):
        """
        Test get all album hashes for further use in the test.
        """
        
        print(ImgurUtil.get_all_albums)

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
        Test deleting many pictures
        """

        pass

    def test_delete_album(self):
        """
        Test delete temporary album
        """

        pass