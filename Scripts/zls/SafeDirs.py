import os

class Dirs:
    def __init__(self, start = None):
        self.olddir = os.getcwd()
        if start != None:
            os.chdir(start)

    def chdir(self, path):
        os.chdir(path)

    def exists(self, path):
        return os.path.exists(path)

    def mkdir(self, path, change = False):
        if not self.exists(path):
            os.mkdir(path)
        if change:
            os.chdir(path)

    def __del__(self):
        os.chdir(self.olddir)
