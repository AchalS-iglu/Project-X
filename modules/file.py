import os

class File():
    def __init__(self, path):
        self.path = path
        self.name = os.path.split(path)
        self.type = os.path.splitext(path)
        self.size = os.path.getsize(path)
        self.ctime = os.path.getctime(path)