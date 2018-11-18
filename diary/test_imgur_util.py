from django.test import TestCase
from utility.imgur import ImgurUtil


class ImgurUtilUploadTest(TestCase):

    def test_01_create_album(self):
        """
        Create a temporary album for testing.
        """

        imgurUtil = ImgurUtil()
        response = imgurUtil.create_album('test_only')
        self.assertEqual(response.status_code, 200)

    def test_02_single_upload(self):
        """
        Test if single upload success.
        """

        imgurUtil = ImgurUtil()
        album_hash = imgurUtil.get_album_hash('test_only')
        imgurUtil.set_album_hash(album_hash)
        image_link = 'https://instagram.fbkk1-2.fna.fbcdn.net/vp/d8d6aa231fb21edf949ff99fbe69fbaf/5C80A671/t51.2885-19/s320x320/38863764_256143965027447_3994031148161302528_n.jpg'
        response = imgurUtil.upload_image('temp', image_link)
        self.assertEqual(response.status_code, 200)

    def test_03_multiple_upload(self):
        """
        Test if multiple upload success.
        """

        imgurUtil = ImgurUtil()
        album_hash = imgurUtil.get_album_hash('test_only')
        imgurUtil.set_album_hash(album_hash)
        image1_link = 'https://instagram.fbkk2-2.fna.fbcdn.net/vp/a7af227dd8e1cf5b352e6bf4b87cefba/5C7A4F55/t51.2885-19/s320x320/42437542_2213514032250422_4515480103911686144_n.jpg'
        image2_link = 'https://instagram.fbkk2-2.fna.fbcdn.net/vp/c7b753a360b321b5968a7e1e7bdead75/5C711690/t51.2885-19/s320x320/28763805_2016317825302323_4003330482501582848_n.jpg'
        image3_link = 'https://instagram.fbkk2-2.fna.fbcdn.net/vp/1f1cf2cea82f1d792ca848f7b5a4597c/5C7562C1/t51.2885-19/s320x320/44392027_1870453886342960_1282978848111067136_n.jpg'
        response1 = imgurUtil.upload_image('temp2', image1_link)
        response2 = imgurUtil.upload_image('temp3', image2_link)
        response3 = imgurUtil.upload_image('temp4', image3_link)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)

    def test_04_create_many_albums(self):
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

    def test_05_get_all_albums(self):
        """
        Test get all album hashes for further use in the test.
        """

        imgurUtil = ImgurUtil()
        response = imgurUtil.get_all_albums_info()
        self.assertEqual(response['status'], 200)

    def test_06_get_single_image(self):
        """
        Test getting an single image from test_album.
        """

        imgurUtil = ImgurUtil()
        album_title = 'test_album'
        album_hash = imgurUtil.get_album_hash(album_title)
        imgurUtil.set_album_hash(album_hash)
        response = imgurUtil.get_image_description('Catterpillar')
        description = 'Catterpillar'
        self.assertEqual(response, description)

    def test_07_get_multiple_image(self):
        """
        Test getting multiple image from test_album.
        """

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

    def test_08_delete_single_image(self):
        """
        Test deleting a picture.
        """

        imgurUtil = ImgurUtil()
        album_hash = imgurUtil.get_album_hash('test_only')
        imgurUtil.set_album_hash(album_hash)
        hashes = imgurUtil.get_image_hash('temp')
        response = imgurUtil.delete_image(hashes)
        self.assertEqual(response.status_code, 200)

    def test_09_delete_multiple_image(self):
        """
        Test deleting many pictures.
        """

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

    def test_10_delete_album(self):
        """
        Test delete an album.
        """

        imgurUtil = ImgurUtil()
        album_title = 'test_only'
        response = imgurUtil.delete_album(album_title)
        self.assertEqual(response.status_code, 200)

    def test_11_delete_multiple_albums(self):
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
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(response3.status_code, 200)

    def test_12_simple_upload_process(self):
        """
        Test whole simple upload process
        """

        imgurUtil = ImgurUtil()
        album_title = 'test_2'
        create_album_response = imgurUtil.create_album(album_title)
        album_hash = imgurUtil.get_album_hash(album_title)
        imgurUtil.set_album_hash(album_hash)
        image_link = 'https://instagram.fbkk1-2.fna.fbcdn.net/vp/d8d6aa231fb21edf949ff99fbe69fbaf/5C80A671/t51.2885-19/s320x320/38863764_256143965027447_3994031148161302528_n.jpg'
        upload_response = imgurUtil.upload_image('test', image_link)
        hashes = imgurUtil.get_image_hash('test')
        delete_image_response = imgurUtil.delete_image(hashes)
        delete_album_response = imgurUtil.delete_album(album_title)
        self.assertEqual(create_album_response.status_code, 200)
        self.assertEqual(upload_response.status_code, 200)
        self.assertEqual(delete_image_response.status_code, 200)
        self.assertEqual(delete_album_response.status_code, 200)

    def test_13_multiple_upload_process(self):
        """
        Test multiple simple upload process
        """

        imgurUtil = ImgurUtil()
        album_title = 'test_3'
        create_album_response = imgurUtil.create_album(album_title)
        album_hash = imgurUtil.get_album_hash(album_title)
        imgurUtil.set_album_hash(album_hash)

        image_link1 = 'https://instagram.fbkk1-1.fna.fbcdn.net/vp/2e312db571e6a0b2eaaba201f54010b5/5C84466C/t51.2885-19/s320x320/26071653_402875793494059_4400556558711259136_n.jpg'
        upload_response1 = imgurUtil.upload_image('test1', image_link1)
        hashes1 = imgurUtil.get_image_hash('test1')

        image_link2 = 'https://instagram.fbkk1-1.fna.fbcdn.net/vp/dca8a4e0ef1508ef6fcc0b9046d6261a/5C896EAC/t51.2885-19/s320x320/43700894_2233080543604526_24320505716670464_n.jpg'
        upload_response2 = imgurUtil.upload_image('test2', image_link2)
        hashes2 = imgurUtil.get_image_hash('test2')

        image_link3 = 'https://instagram.fbkk1-1.fna.fbcdn.net/vp/dde581ed788603a79d4d3f73a40bc132/5C8846B6/t51.2885-19/s320x320/43661432_2011354002276624_8575559070172315648_n.jpg'
        upload_response3 = imgurUtil.upload_image('test3', image_link3)
        hashes3 = imgurUtil.get_image_hash('test3')

        delete_image_response1 = imgurUtil.delete_image(hashes1)
        delete_image_response2 = imgurUtil.delete_image(hashes2)
        delete_image_response3 = imgurUtil.delete_image(hashes3)

        delete_album_response = imgurUtil.delete_album(album_title)
        self.assertEqual(create_album_response.status_code, 200)

        self.assertEqual(upload_response1.status_code, 200)
        self.assertEqual(upload_response2.status_code, 200)
        self.assertEqual(upload_response3.status_code, 200)

        self.assertEqual(delete_image_response1.status_code, 200)
        self.assertEqual(delete_image_response2.status_code, 200)
        self.assertEqual(delete_image_response3.status_code, 200)

        self.assertEqual(delete_album_response.status_code, 200)
