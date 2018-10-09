from PIL import Image
import os.path
import re

def scaleImageTo(name, max_size):
    raw_image = Image.open(name)
    raw_image.thumbnail(max_size, Image.ANTIALIAS)
    return raw_image

def findBestMatch(r, g, b, t):
    pass

def configExists(path):
    return os.path.isfile(path)

def createConfig(path):
    averages = []
    
    with open("materials.txt", "r") as materials:
        for line in materials:
            image_name, true_id = getLineProps(line)
            image = Image.open("./blocks/"+image_name)
            pic = image.load()
            
            width, height = image.size
            r, g, b = getAverageColor(width, height, pic)
            
            block_info = {"name": image_name, "id": true_id, "rgb": (r, g, b)}
            averages.append(block_info)
    print(averages)
            
def getLineProps(line):
    line_values = line.split(",")
    image_name = re.findall("(?<=,)[^,]*\.png", line)[0]
    
    true_id = ""
    primary_id = line_values[3]
    secondary_id = line_values[4]
    if secondary_id == "0":
        true_id = primary_id
    else:
        true_id = primary_id+":"+secondary_id
    
    return image_name, true_id


def getAverageColor(x, y, image):
    """ Returns a 3-tuple containing the RGB value of the average color of the
    given square bounded area of length = n whose origin (top left corner) 
    is (x, y) in the given image"""
 
    r, g, b = 0, 0, 0
    count = 0
    for s in range(x):
        for t in range(y):
            pixlr, pixlg, pixlb, pixlt = image[s, t]
            r += pixlr
            g += pixlg
            b += pixlb
            count += 1
    return ((r/count), (g/count), (b/count))


