__author__ = 'gmena'
import uuid
import base64

from PIL import Image
from lib import File


class Img(File):
    img = None
    output = None
    name = None
    is_valid_format = False

    def __init__(self, img):
        """
        Initialize the Image Class
        :param img:binary
        """
        super(self.__class__, self).__init__(img)
        self.img = self.handle_uploaded_file()
        try:
            self.img = Image.open(self.img)
            self.is_valid_format = True
            self.name = self.prepare_image_name(self.file.name)
            self.output = self.tmp_dir
        except IOError:
            pass

    def prepare_image_name(self, name):
        """
        Simplify name to image
        :param name:string
        :return: string
        """
        return base64.urlsafe_b64encode(name) + '.' + self.get_file_format()

    def get_image(self):
        """
        Return the Image Object
        :return:object
        """
        return self.img

    def set_output_dir(self, output):
        """
        Set the image directory
        :param output:string
        """
        self.output = output

    def get_output_dir(self):
        """
        Return the image directory
        :return:string
        """
        return self.output

    def set_file_name(self, name):
        """
        Change auto-naming image file result
        :param name:string
        """
        self.name = self.prepare_image_name(name)

    def get_file_name(self):
        """
        Return the file name
        :return:string
        """
        return self.name.lower()

    def get_file_format(self):
        """
        Return the image format
        :return:string
        """
        return self.img.format

    def is_valid_image(self):
        """
        Is a valid image?
        :return:bool
        """
        return self.is_valid_format

    def thumb_create(self, width=64, height=64):
        """
        Resize Image
        :param width:int
        :param height:int
        :return:string
        """
        prefix = uuid.uuid1().hex[:8].lower()
        size = (width, height)
        self.name = prefix + self.get_file_name()

        thumb_dir = self.get_output_dir() + '/' + self.name

        new_image = self.img.copy()
        new_image.thumbnail(size)
        new_image.save(thumb_dir, self.get_file_format())

        return thumb_dir

    def crop_with_coords(self, x1, y1, x2, y2):
        """
        Crop Image
        :param x1:int
        :param y1:int
        :param x2:int
        :param y2:int
        """
        box = (x1, y1, x2, y2)
        region = self.img.crop(box)
        region = region.transpose(Image.ROTATE_180)
        self.img.paste(region, box)
