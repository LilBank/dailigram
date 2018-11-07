from imgurpython import ImgurClient
from decouple import config
import requests


class ImgurUtil:

    imgur_id = config('IMGUR_CLIENT_ID')
    imgur_key = config('IMGUR_SECRET_KEY')
    imgur_username = config('IMGUR_USERNAME')
    client = ImgurClient(imgur_id, imgur_key)
    token = config('ACCESS_TOKEN')

    def create_album(self, albumTitle):
        """
        Create a album with the name from parameter.
        """

        url = 'https://api.imgur.com/3/album/'
        payload = '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"title\"\r\n\r\n' + albumTitle + '\r\n'
        headers = {
            'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW',
            'Authorization': 'Bearer '+ImgurUtil.token
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        return response

    def delete_album(self, albumTitle):
        """
        Delete the album with the album hash.
        """
        albumHash = self.get_album_hash(albumTitle)
        url = 'https://api.imgur.com/3/album/' + albumHash
        headers = {'Authorization': 'Bearer ' + ImgurUtil.token}
        response = requests.request("DELETE", url, headers=headers)
        return response.json()

    def get_image_info(self, albumHash, imageHash):
        """
        Get image info as json.
        """

        url = 'https://api.imgur.com/3/album/' + albumHash + '/image/' + imageHash
        headers = {'Authorization': 'Bearer ' + ImgurUtil.token}
        response = requests.request("GET", url, headers=headers)
        return response.json()

    def get_image_link(self, albumHash, imageHash):
        """
        Get the link of the image.
        """

        image_info = self.get_image_info(albumHash, imageHash)
        return image_info['data']['link']

    def get_image_description(self, albumHash, imageHash):
        """
        Get the description of the image.
        """

        image_info = self.get_image_info(albumHash, imageHash)
        return image_info['data']['description']

    def get_all_albums_info(self):
        """
        Get information of every albums as json.
        """

        url = 'https://api.imgur.com/3/account/'+ImgurUtil.imgur_username+'/albums/'
        headers = {'Authorization': 'Bearer ' + ImgurUtil.token}
        response = requests.request("GET", url, headers=headers)
        return response.json()

    def get_album_hash(self, albumTitle):
        """
        Get album hash by album title.
        """

        albums = self.get_all_albums_info()
        temp_list = albums['data']
        for single_dict in temp_list:
            if single_dict['title'] == albumTitle:
                tempHash = single_dict['id']
                return tempHash

    def upload_image(self, albumTitle, id):
        """
        Upload image to the selected album with an id.
        """

        # url = 'https://api.imgur.com/3/album/'+albumTitle+'/add'
        # payload = '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ids[]\"\r\n\r\n{{imageHash}}\r\n'
        # headers = {
        #     'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW',
        #     'Authorization': 'Bearer {{accessToken}}'
        # }
        # response = requests.request("POST", url, data=payload, headers=headers)
        # return response
