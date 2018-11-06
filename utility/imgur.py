from imgurpython import ImgurClient
from decouple import config
import requests


class ImgurUtil:

    imgur_id = config('IMGUR_CLIENT_ID')
    imgur_key = config('IMGUR_SECRET_KEY')
    client = ImgurClient(imgur_id, imgur_key)
    token = config('ACCESS_TOKEN')
    albumHash = ''
    imageHash = ''

    def get_all_homepage_image(*args):
        """
        Get all current images from Imgur homepage.
        """

        items = ImgurUtil.client.gallery()
        return items

    def get_image_info(self):
        """
        Get image info as json.
        """

        url = 'https://api.imgur.com/3/album/' + \
            ImgurUtil.albumHash + '/image/' + ImgurUtil.imageHash
        headers = {'Authorization': 'Bearer ' + ImgurUtil.token}
        response = requests.request("GET", url, headers=headers)
        return response.json()

    def get_image_link(self):
        """
        Get the link of the image.
        """

        return ImgurUtil.get_image_info('')['data']['link']

    def get_image_description(self):
        """
        Get the description of the image.
        """

        return ImgurUtil.get_image_info('')['data']['description']

    def create_album(self, albumName):
        url = 'https://api.imgur.com/3/album'
        payload = '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n'+ albumName +'\r\n'
        headers = {
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW',
            'Authorization': 'Bearer '+ImgurUtil.token
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        return response

    def set_albumHash(self, hash):
        """
        Set album hash.
        """
        ImgurUtil.albumHash = hash

    def set_imageHash(self, hash):
        """
        Set image hash.
        """

        ImgurUtil.imageHash = hash
