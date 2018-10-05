from PIL import Image
import os.path

def scaleImageTo(name, max_size):
    raw_image = Image.open(name)
    raw_image.thumbnail(max_size, Image.ANTIALIAS)
    return raw_image

def findBestMatch(r, g, b, t):
    pass

def configExists(path):
    return os.path.isfile("path")

def createConfig(path):
    pass