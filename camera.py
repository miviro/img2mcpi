from picamera import PiCamera
from utils import *

camera = PiCamera()
image_name = "photo.png"
max_size = (128, 128)
config_path = "./config.json" 

if not configExists(config_path):
    print("Config file not found. Creating...")
    createConfig(config_path)
print("Using config file.")
averages = readConfig(config_path)

print("Taking photo...")
camera.capture(image_name)
print("Rescaling image...")
scaled_image = scaleImageTo(image_name, max_size)

loaded_image = scaled_image.load()
width, height = scaled_image.size
print("Scaled photo dimensions: ", width, height)
print("Getting optimal blocks...")
for x in range(width):
    for y in range(height):
        r, g, b, t = loaded_image[x, y]
        best_match = findBestMatch(r, g, b, averages)
        print(best_match)