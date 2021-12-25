import os

class File():
    def __init__(self, path):
        self.path = path
        self.name = os.path.split(path)[1]
        self.title = os.path.splitext(path)[0]
        self.type = os.path.splitext(path)[1]
        self.size = os.path.getsize(path)
        self.ctime = os.path.getctime(path)