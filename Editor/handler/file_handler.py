# klasa koja je zaduzena za brisanje u projektu i kreiranje nove datoteke
import os
from genericpath import isdir


class FileHandler(object):
    def __init__(self):

        super(FileHandler, self).__init__()

    def create_file(self, path, name):
        open(os.path.join(path, name), mode='w').close()

    def remove_file(self, path):
        os.remove(os.path.join(path))

    def rename(self, path, oldName, newName):
        os.rename(os.path.join(path, oldName), os.path.join(path, newName))

    def get_type(self, path):
        if isdir(path):
            return 'FOLDER '
        else:
            return 'FILE '
