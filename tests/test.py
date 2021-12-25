import projectx.helpers.uploaders.imgur as imgur
from projectx.modules.file import File

tortle = File('tortle.jpg')
print(imgur.upload(tortle))