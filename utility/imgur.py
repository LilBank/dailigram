from imgurpython import ImgurClient
from decouple import config
from PIL import Image
import requests
import base64
import json
import pyimgur


class ImgurUtil:

    imgur_id = config('IMGUR_CLIENT_ID')
    imgur_key = config('IMGUR_SECRET_KEY')
    imgur_username = config('IMGUR_USERNAME')
    client = ImgurClient(imgur_id, imgur_key)
    token = config('ACCESS_TOKEN')
    album_hash = ''

    def create_album(self, album_title):
        """
        Create a album with the name from parameter.
        """

        url = 'https://api.imgur.com/3/album/'
        payload = '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n' + album_title + '\r\n'
        headers = {
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW',
            'Authorization': 'Bearer '+self.token,
            'cache-control': 'no-cache',
            'Postman-Token': 'ca8ef2de-4539-4300-a986-befe6bc35e54'
        }
        response = requests.request('POST', url, data=payload, headers=headers)
        return response

    def delete_image(self, image_hash):
        """
        Delete the wanted image by the image hash
        """

        url = 'https://api.imgur.com/3/image/'+image_hash
        headers = {
            'Authorization': 'Bearer '+self.token,
            'cache-control': 'no-cache',
            'Postman-Token': '7b73f3b5-8197-4d0e-8de4-d2cfdae03f8d'
            }
        response = requests.request('DELETE', url, headers=headers)
        return response

    def delete_album(self, album_title):
        """
        Delete the album with the album hash.
        """
        hashes = self.get_album_hash(album_title)
        url = 'https://api.imgur.com/3/album/' + hashes
        headers = {
            'Authorization': 'Bearer ' + self.token,
            'cache-control': 'no-cache',
            'Postman-Token': 'd56eb26f-4244-4e28-8632-7679f8182c2c'
            }
        response = requests.request('DELETE', url, headers=headers)
        return response

    # Private
    def get_images_from_albums(self):
        """
        Get all images from the album.
        """

        url = 'https://api.imgur.com/3/album/'+self.album_hash+'/images'
        headers = {
            'Authorization': 'Bearer ' + self.token,
            'cache-control': 'no-cache',
            'Postman-Token': '57839a20-e3da-4ec0-87a7-b4d675391513'
            }
        response = requests.request('GET', url, headers=headers)
        return response.json()

    # Private
    def get_image_info(self, description):
        """
        Get the image information by description.
        """

        images = self.get_images_from_albums()
        temp_list = images['data']
        for single_dict in temp_list:
            if single_dict['description'] == description:
                temp_dict = single_dict
                return temp_dict

    def get_image_link(self, description):
        """
        Get the link of the image.
        """

        image_info = self.get_image_info(description)
        return image_info['link']

    def get_image_description(self, description):
        """
        Get the description of the image.
        """

        image_info = self.get_image_info(description)
        return image_info['description']

    def get_image_hash(self, description):
        """
        Get the description of the image.
        """

        image_info = self.get_image_info(description)
        return image_info['id']

    # Private
    def get_all_albums_info(self):
        """
        Get information of every albums as json.
        """

        url = 'https://api.imgur.com/3/account/'+self.imgur_username+'/albums/'
        headers = {
            'Authorization': 'Bearer ' + self.token,
            'cache-control': 'no-cache',
            'Postman-Token': '0a988d32-8dc2-408a-9826-52551e853045'
            }
        response = requests.request('GET', url, headers=headers)
        return response.json()

    # Private
    def get_album_hash(self, album_title):
        """
        Get album hash by album title.
        """

        albums = self.get_all_albums_info()
        temp_list = albums['data']
        for single_dict in temp_list:
            if single_dict['title'] == album_title:
                temp_hash = single_dict['id']
                return temp_hash

    def upload_image(self, description, image_destination):
        """
        Upload image to the selected album with a description.
        """

        url = "https://api.imgur.com/3/image"
        payload = '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"image\"\r\n\r\n'+image_destination + \
            '\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"album\"\r\n\r\n'+self.album_hash + \
            '\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n'+description + \
            '\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--'
        headers = {
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW',
            'Authorization': 'Bearer '+self.token,
            'cache-control': 'no-cache',
            'Postman-Token': 'de7cd513-ded5-4102-b869-3f5f5af4d402'
        }
        response = requests.request('POST', url, data=payload, headers=headers)
        return response

    def set_album_hash(self, album_hash):
        """
        Set a default album hash.
        """

        self.album_hash = album_hash
