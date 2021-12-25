import src.uploaders.imgur as imgur
from src.modules.file import File

tortle = File('tortle.jpg')
print(imgur.upload(tortle))