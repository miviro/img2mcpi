from picamera import PiCamera
from PIL import Image

def scaleImageTo(name, max_size):
    raw_image = Image.open(name)
    raw_image.thumbnail(max_size, Image.ANTIALIAS)
    return raw_image

camera = PiCamera()
image_name = "photo.png"
max_size = (128, 128)

camera.capture(image_name)
scaled_image = scaleImageTo(image_name, max_size)
