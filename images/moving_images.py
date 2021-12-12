from PIL import Image
import os

def move_image(imageLocation : str, newLocationFolder : str):
    """Moves a image to a new folder

    Args:
        imageLocation (str): The image you want to move, requires full file path to image
        newLocationFolder (str): The location you want the file to be saved to, requires full folder path
    """
    
    location = imageLocation.split("/")
    
    file = location[-1]
    
    if newLocationFolder[-1] != "/":
        newLocationFolder += "/"
    
    newLocation = newLocationFolder + file
    
    with Image.open(imageLocation) as img:
        img.save(newLocation)
