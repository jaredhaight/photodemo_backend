from PIL import Image, ImageOps
from photodemo_backend.settings import MEDIA_ROOT

def resize_image(image, height, width):
    slash = image.name.find('/')+1
    dot = image.name.find('.')
    filename = MEDIA_ROOT+'crops/'+str(image.name[slash:dot])+'_h'+str(height)+'_w'+str(width)+'.jpg'
    t_img = Image.open(image.path)
    if width == 0:
        width = t_img.size[0] * height / t_img.size[1]
    if height == 0:
        height = t_img.size[1] * width / t_img.size[0]
    t_img.thumbnail((width,height), Image.ANTIALIAS)
    t_img.save(filename, 'JPEG', quality=95)

    return filename

def get_orientation(image):
        width = image.width
        height = image.height

        if width > height:
            return 'landscape'

        if width < height:
            return 'portrait'