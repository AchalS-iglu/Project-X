import requests
from imgurpython import ImgurClient

from tokens import IMGUR_CLIENT_ID, IMGUR_CLIENT_SECRET

class Imgur():
    def __init__(self):
        self.client = ImgurClient(IMGUR_CLIENT_ID, IMGUR_CLIENT_SECRET)
        
    def upload(self, image):
        image = self.client.upload_from_path(image.path, anon=True)
        return image