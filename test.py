from modules.file import File
from src.uploaders.imgur import Imgur
from src.modules.file import File

imgur = Imgur()

tortle = File('tortle.jpg')
print(imgur.upload(tortle))