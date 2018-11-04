from imgurpython import ImgurClient
from decouple import config
import requests

class ImgurUtil:

    imgur_id = config('IMGUR_CLIENT_ID')
    imgur_key = config('IMGUR_SECRET_KEY')
    client = ImgurClient(imgur_id, imgur_key)

    # def authenticate(self):
    #     imgur_username = config('IMGUR=USERNAME')
    #     imgur_password = config('IMGUR=PASSWORD')
    #     client.set_user_auth()

    def get_all_homepage_image(self):
        items = ImgurUtil.client.gallery()
        return items

    def get_image_link(self):

        url = 'https://api.imgur.com/3/album/{{albumHash}}/image/{{imageHash}}'

        headers = {'Authorization': 'Client-ID {{clientId}}'}

        response = requests.request("GET", url, headers=headers)

        return response.link
