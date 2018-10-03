from picamera import PiCamera
from PIL import Image
from utils import *

camera = PiCamera()
image_name = "photo.png"
max_size = (128, 128)

camera.capture(image_name)
scaled_image = scaleImageTo(image_name, max_size)

loaded_image = scaled_image.load()
width, height = scaled_image.size
for i in range(width):
    for j in range(height):
        print(loaded_image[i, j])