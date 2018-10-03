from picamera import PiCamera
from utils import *

camera = PiCamera()
image_name = "photo.png"
max_size = (128, 128)

camera.capture(image_name)
scaled_image = scaleImageTo(image_name, max_size)
