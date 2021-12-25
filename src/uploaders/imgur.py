from imgurpython import ImgurClient

from tokens import IMGUR_CLIENT_ID, IMGUR_CLIENT_SECRET

    
def upload(image):
    client =ImgurClient(IMGUR_CLIENT_ID, IMGUR_CLIENT_SECRET)
    config = {
        'name': image.name,
        'title': image.title
    }
    image = client.upload_from_path(image.path, config=config, anon=True)
    return image