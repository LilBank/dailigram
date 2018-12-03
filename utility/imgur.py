from imgurpython import ImgurClient
from decouple import config
import requests
from singleton_decorator import singleton
from decouple import config

@singleton
class ImgurUtil:

    token = config('ACCESS_TOKEN')
    album_hash = config('ALBUM_HASH')

    # Public
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
        }
        response = requests.request('POST', url, data=payload, headers=headers)
        return response

    # Public
    def delete_image(self, image_hash):
        """
        Delete the wanted image by the image hash
        """

        url = 'https://api.imgur.com/3/image/'+image_hash
        headers = {
            'Authorization': 'Bearer '+self.token,
            'cache-control': 'no-cache',
        }
        response = requests.request('DELETE', url, headers=headers)
        return response

    # Public
    def delete_album(self, album_title):
        """
        Delete the album with the album hash.
        """
        hashes = self.get_album_hash(album_title)
        url = 'https://api.imgur.com/3/album/' + hashes
        headers = {
            'Authorization': 'Bearer ' + self.token,
            'cache-control': 'no-cache',
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

    # Publlic
    def get_image_link(self, description):
        """
        Get the link of the image by description.
        """

        image_info = self.get_image_info(description)
        return image_info['link']

    # Public
    def get_image_description(self, description):
        """
        Get the description of the image which @param description
        is use in function get_image_info(description).
        """

        image_info = self.get_image_info(description)
        return image_info['description']

    # Public

    def get_image_hash(self, description):
        """
        Get the hash of the image.
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
        }
        response = requests.request('GET', url, headers=headers)
        return response.json()

    # Public
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

    # Public
    def upload_image(self, description, image_url):
        """
        Upload image to the album with a description which image source is a link. 
        Album destination is the album set from function set_album_hash.
        """

        url = "https://api.imgur.com/3/image"
        payload = '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"image\"\r\n\r\n'+image_url + \
            '\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"album\"\r\n\r\n'+self.album_hash + \
            '\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"description\"\r\n\r\n'+description + \
            '\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--'
        headers = {
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW',
            'Authorization': 'Bearer '+self.token,
            'cache-control': 'no-cache',
        }
        response = requests.request('POST', url, data=payload, headers=headers)
        return response

    # Public
    def upload_image_locally(self, description, image_source):
        """
        Upload image to the album with a description which image source is a picture's file. 
        Album destination is the album set from function set_album_hash.
        """
        url = "https://api.imgur.com/3/image"
        files = {"image": image_source}
        body = {
            'album': self.album_hash,
            'description': description,
        }
        headers = {
            'Authorization': 'Bearer ' + self.token,
            'cache-control': 'no-cache',
        }
        response = requests.post(url, files=files, headers=headers, data=body)
        return response
