from picamera import PiCamera
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from utils import *
from PIL import Image

print("Connecting to Minecraft")
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
pos = minecraft.Vec3(pos.x, pos.y, pos.z)

max_size = (64, 64)
config_path = "./config.json"
scaled_image = None
image_name = "photo.png"
scaled_name = "sphoto.png"

custom_path = input("Select image path. Empty for camera image: ")
if custom_path == "":
    camera = PiCamera()

    print("Taking photo...")
    camera.capture(image_name)
else:
    image_name = custom_path

if not configExists(config_path):
    print("Config file not found. Creating...")
    createConfig(config_path)

print("Using config file.")
averages = readConfig(config_path)

print("Rescaling image...")
scaled_image = scaleImageTo(image_name, max_size)
scaled_image.save(scaled_name)

loaded_image = scaled_image.load()
width, height = scaled_image.size
print("Scaled photo dimensions: ", width, height)
print("Getting optimal blocks...")

temp_pos = pos
for y in range(height):
    for x in range(width):
        temp_pos = minecraft.Vec3(temp_pos.x+1, temp_pos.y, temp_pos.z)
        r, g, b, t = loaded_image[x, y]

        full_best_match = findBestMatch(r, g, b, averages)
        best_match_id = full_best_match[0]

        # If there is only one item in full_best_match, assume the item is a simple ID
        if len(full_best_match) == 1:
            mc.setBlock(temp_pos, float(best_match_id))
        # Else add the sub-id as an argument
        else:
            mc.setBlock(temp_pos, float(best_match_id), float(full_best_match[1]))

    temp_pos = minecraft.Vec3(pos.x, temp_pos.y+1, temp_pos.z)
    # Slow down to prevent connection losses
    time.sleep(1)