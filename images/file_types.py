from PIL import Image
import os, sys

def jpeg_to_webp(imageLocation : str, newLocationFolder : str):
    """Transforms a jpeg (jpg) into a webp image

    Args:
        imageLocation (str): The image you want to change to a webp location, requires full path to image
        newLocationFolder (str): The location you want the file to be saved to, requires full folder path
    """
    location = imageLocation.split("/") # Splits the orginal image path into parts
    
    f, e = os.path.splitext(location[-1]) # Splits the extention away from the filename
    
    outfile = f + ".webp" # Adds the '.webp' to file name
    
    newLocation = newLocationFolder + outfile # Sets new location and filename into a variable // This is just to make it look nice
    
    with Image.open(imageLocation) as img:
        img.save(newLocation) # Opens and saves new image into file location
    
def webp_to_jpeg(image, location):
    """Transforms a webp image into a jpeg (jpg)

    Args:
        imageLocation (str): The image you want to change to a webp location, requires full path to image
        newLocationFolder (str): The location you want the file to be saved to, requires full folder path
    """
    location = imageLocation.split("/") # Splits the orginal image path into parts
    
    f, e = os.path.splitext(location[-1]) # Splits the extention away from the filename
    
    outfile = f + ".jpeg" # Adds the '.webp' to file name
    
    newLocation = newLocationFolder + outfile # Sets new location and filename into a variable // This is just to make it look nice
    
    with Image.open(imageLocation) as img:
        img.save(newLocation) # Opens and saves new image into file location
