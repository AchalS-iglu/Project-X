from modules.file import File
from uploaders.imgur import Imgur
from modules.file import File

imgur = Imgur()

tortle = File('tortle.jpg')
print(imgur.upload(tortle))