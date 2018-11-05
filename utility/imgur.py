from imgurpython import ImgurClient
from decouple import config
import requests


class ImgurUtil:

    imgur_id = config('IMGUR_CLIENT_ID')
    imgur_key = config('IMGUR_SECRET_KEY')
    client = ImgurClient(imgur_id, imgur_key)

    def get_all_homepage_image(*args):
        items = ImgurUtil.client.gallery()
        return items

    def get_image_info(self,albumHash,imageHash):

        token = config('ACCESS_TOKEN')

        url = 'https://api.imgur.com/3/album/{{albumHash}}/image/{{imageHash}}'

        headers = {'Authorization': 'Bearer {{token}}'}

        response = requests.request("GET", url, headers=headers)

        return response
