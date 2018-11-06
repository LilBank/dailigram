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
        items = ImgurUtil.client.gallery()
        return items

    def get_image_info(self):
        url = 'https://api.imgur.com/3/album/' + ImgurUtil.albumHash + '/image/'+ ImgurUtil.imageHash
        headers = {'Authorization': 'Bearer ' + ImgurUtil.token }
        response = requests.request("GET", url, headers=headers)
        # print(headers)
        # print(url)
        # print(ImgurUtil.albumHash)
        # print(ImgurUtil.imageHash)
        # print(ImgurUtil.token)
        return response.json()

    def get_image_link(self):
        return ImgurUtil.get_image_info('')['data']['link']

    def get_image_description(self):
        return ImgurUtil.get_image_info('')['data']['description']

    def set_albumHash(self, hash):
        ImgurUtil.albumHash = hash

    def set_imageHash(self, hash):
        ImgurUtil.imageHash = hash
