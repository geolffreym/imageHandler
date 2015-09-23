__author__ = 'gmena'
import shutil
import os


class File(object):
    tmp_dir = '/tmp'
    local_dir = None
    file = None

    def __init__(self, file):
        self.file = file

    def handle_uploaded_file(self):
        """
        Join incoming file with chunks
        :return:string
        """""
        name = self.file.name
        local_dir = self.tmp_dir + '/' + name

        with open(local_dir, 'wb+') as destiny:
            for chunk in self.file.chunks():
                destiny.write(chunk)

        self.local_dir = local_dir
        return self.local_dir

    def get_file_dir(self):
        """
        Return the file fir
        :return:string
        """""
        return self.local_dir

    @staticmethod
    def copy_file(dirt, new_dir):
        """
        Copy file from directory to directory
        :param dirt:string
        :param new_dir:string
        :return:bool
        """""
        return shutil.copy(dirt, new_dir)

    @staticmethod
    def move_file(dirt, new_dir):
        """
        Move file from directory to directory
        :param dirt:string
        :param new_dir:string
        :return:bool
        """""
        return shutil.move(dirt, new_dir)

    @staticmethod
    def remove_file(dirt):
        """
        Remove file from system
        :param dirt:string
        :return:bool
        """""
        return os.remove(dirt)
