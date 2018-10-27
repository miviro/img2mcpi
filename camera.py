from picamera import PiCamera
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
from utils import *
from PIL import Image

print("Connecting to Minecraft")
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
pos = minecraft.Vec3(float(pos.x), float(pos.y), float(pos.z))
max_size = (64, 64)
config_path = "./config.json"
scaled_image = None
image_name = "photo.png"
scaled_name = "sphoto.png"

n_name = input("Select image path. Empty for camera image: ")
if n_name == "":
    camera = PiCamera()
    
    print("Taking photo...")
    camera.capture(image_name)
else:
    image_name = n_name

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

tpos = pos
for y in range(height):
    for x in range(width):
        tpos = minecraft.Vec3(tpos.x+1, tpos.y, tpos.z)
        r, g, b, t = loaded_image[x, y]
        t_best_match = findBestMatch(r, g, b, averages)
        best_match = t_best_match[0]
        
        if len(t_best_match) == 1:
            mc.setBlock(tpos, float(best_match))
        else:
            mc.setBlock(tpos, float(best_match), float(t_best_match[1]))
        
    tpos = minecraft.Vec3(pos.x, tpos.y+1, tpos.z)
    time.sleep(1)