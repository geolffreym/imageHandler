__author__ = 'gmena'

from lib.Image import Img


def get_valid_img(index, obj):
    if index in obj.request.FILES:
        img = Img(obj.request.FILES[index])
        if not img.is_valid_image():
            return False
        return img
    return None
