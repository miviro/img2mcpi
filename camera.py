from picamera import PiCamera
from PIL import Image

def scaleImageTo(name, max_size):
    raw_image = Image.open(name)
    raw_image.thumbnail(max_size, Image.ANTIALIAS)
    raw_image.save(name, "PNG")

camera = PiCamera()
image_name = "photo.png"
max_size = (256, 256)

camera.capture(image_name)
scaleImageTo(image_name, max_size)
