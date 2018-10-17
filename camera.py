from picamera import PiCamera
import mcpi.minecraft as minecraft
import mcpi.block as block
from utils import *

print("Connecting to Minecraft")
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
pos = minecraft.Vec3(float(pos.x+20), float(pos.y), float(pos.z))

camera = PiCamera()
image_name = "photo.png"
max_size = (8, 8)
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
        t_best_match = findBestMatch(r, g, b, averages)
        best_match = t_best_match[0]
        
        if len(t_best_match) == 1:
            mc.setBlock(pos, float(best_match))
        else:
            mc.setBlock(pos, float(best_match), float(t_best_match[1]))
        
        pos = minecraft.Vec3(float(pos.x), float(pos.y), float(pos.z+1))
    pos = minecraft.Vec3(float(pos.x), float(pos.y+1), float(pos.z))