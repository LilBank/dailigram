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


class ViewTest(TestCase):

    def test_accessible_by_name(self):
        """
        Test diary's existance by the response status code.
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_accessible_by_location(self):
        response = self.client.get('/accounts/diary/')
        self.assertEqual(response.status_code, 200)

    def test_no_diary_by_view(self):
        """
        Test that the total context object is 0 when nothing is inserted.
        """
        response = self.client.get(reverse('diary:login'))
        self.assertQuerysetEqual(response.context['all_diarys'], [])
    
    def test_login(self):
        """
        Test if the login is sucess or not
        """
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)

class FormTest(TestCase):

    def test_valid_forms(self):
        """
        Test if the form is valid or not.
        """
        form  = UserForm()
        self.assertTrue(form.is_valid)


class ImgurUtilUploadTest(TestCase):

    def test_create_album(self):
        """
        Create a temporary album for testing.
        """
        print('test create an album')
        imgurUtil = ImgurUtil()
        response = imgurUtil.create_album('test_only')
        self.assertEqual(response.status_code, 200)

    def test_single_upload(self):
        """
        Test if single upload success.
        """
        print('test single uploads')
        imgurUtil = ImgurUtil()
        album_hash = imgurUtil.get_album_hash('test_only')
        imgurUtil.set_album_hash(album_hash)
        image_link = 'https://instagram.fbkk1-2.fna.fbcdn.net/vp/d8d6aa231fb21edf949ff99fbe69fbaf/5C80A671/t51.2885-19/s320x320/38863764_256143965027447_3994031148161302528_n.jpg'
        response = imgurUtil.upload_image('temp', image_link)
        self.assertEqual(response.status_code, 200)

    def test_multiple_upload(self):
        """
        Test if multiple upload success.
        """
        print('test multiple uploads')
        imgurUtil = ImgurUtil()
        album_hash = imgurUtil.get_album_hash('test_only')
        imgurUtil.set_album_hash(album_hash)
        image1_link = 'https://instagram.fbkk2-2.fna.fbcdn.net/vp/a7af227dd8e1cf5b352e6bf4b87cefba/5C7A4F55/t51.2885-19/s320x320/42437542_2213514032250422_4515480103911686144_n.jpg'
        image2_link ='https://instagram.fbkk2-2.fna.fbcdn.net/vp/c7b753a360b321b5968a7e1e7bdead75/5C711690/t51.2885-19/s320x320/28763805_2016317825302323_4003330482501582848_n.jpg'
        image3_link ='https://instagram.fbkk2-2.fna.fbcdn.net/vp/1f1cf2cea82f1d792ca848f7b5a4597c/5C7562C1/t51.2885-19/s320x320/44392027_1870453886342960_1282978848111067136_n.jpg'
        response1 = imgurUtil.upload_image('temp2', image1_link)
        response2 = imgurUtil.upload_image('temp3', image2_link)
        response3 = imgurUtil.upload_image('temp4', image3_link)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)

    def test_create_many_albums(self):
        """
        Create many albums for testing.
        """
        print('create an album')
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
        print('test get all albums')
        imgurUtil = ImgurUtil()
        response = imgurUtil.get_all_albums_info()
        self.assertEqual(response['status'], 200)     

    def test_get_single_image(self):
        """
        Test getting an single image from test_album.
        """

        print('test get single image')
        imgurUtil = ImgurUtil()
        album_title = 'test_album'
        album_hash = imgurUtil.get_album_hash(album_title)
        imgurUtil.set_album_hash(album_hash)
        response = imgurUtil.get_image_description('Catterpillar')
        description = 'Catterpillar'
        self.assertEqual(response, description)

    def test_get_multiple_image(self):
        """
        Test getting multiple image from test_album.
        """
        print('test get multiple image')
        imgurUtil = ImgurUtil()
        album_title = 'test_album'
        album_hash = imgurUtil.get_album_hash(album_title)
        imgurUtil.set_album_hash(album_hash)

 
        des1 = 'Catterpillar'
        image1_des = imgurUtil.get_image_description(des1)


        des2 = 'Sea and mountain'
        image2_des = imgurUtil.get_image_description(des2)


        des3 = 'Catty'
        image3_des = imgurUtil.get_image_description(des3)

        self.assertEqual(image1_des, des1)
        self.assertEqual(image2_des, des2)
        self.assertEqual(image3_des, des3)

    def test_delete_single_image(self):
        """
        Test deleting a picture.
        """
        print('delete single image')
        imgurUtil = ImgurUtil()
        album_hash = imgurUtil.get_album_hash('test_only')
        imgurUtil.set_album_hash(album_hash)
        hashes = imgurUtil.get_image_hash('temp')
        response = imgurUtil.delete_image(hashes)
        self.assertEqual(response.status_code, 200)


    def test_delete_multiple_image(self):
        """
        Test deleting many pictures.
        """
        print('test delete multiple image')
        imgurUtil = ImgurUtil()
        album_hash = imgurUtil.get_album_hash('test_only')
        imgurUtil.set_album_hash(album_hash)
        hashes2 = imgurUtil.get_image_hash('temp2')
        hashes3 = imgurUtil.get_image_hash('temp3')
        hashes4 = imgurUtil.get_image_hash('temp4')
        response1 = imgurUtil.delete_image(hashes2)
        response2 = imgurUtil.delete_image(hashes3)
        response3 = imgurUtil.delete_image(hashes4)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)
        

    def test_delete_album(self):
        """
        Test delete an album.
        """
        print('test delete single album')
        imgurUtil = ImgurUtil()
        album_title = 'test_only'
        response = imgurUtil.delete_album(album_title)
        self.assertEqual(response.status_code, 200)

    def test_delete_multiple_albums(self):
        """
        Test delete many albums.
        """
        print('test delete many albums')
        imgurUtil = ImgurUtil()
        albumTitle_1 = 'album1'
        albumTitle_2 = 'album2'
        albumTitle_3 = 'album3'
        response1 = imgurUtil.delete_album(albumTitle_1)
        response2 = imgurUtil.delete_album(albumTitle_2)
        response3 = imgurUtil.delete_album(albumTitle_3)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)
