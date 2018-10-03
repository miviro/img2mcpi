from PIL import Image

def scaleImageTo(name, max_size):
    raw_image = Image.open(name)
    raw_image.thumbnail(max_size, Image.ANTIALIAS)
    return raw_image