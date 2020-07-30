from PIL import Image
import glob
import numpy as np
# from zenith.grid import grid
import io
Image.MAX_IMAGE_PIXELS = 350000000000000


# Improting Image class from PIL module 
from PIL import Image 
import numpy as np
# Opens a image in RGB mode 
from zenith.grid import grid

import pytest

def test_grid():
    
    output_directory = 'output'

    overlap_percentage = 50
    img_width = 250
    img_height = 250
    file_name = 'test_image.png'
    print(file_name)
    number_of_grid = grid(file_name,img_width,img_height,overlap_percentage,output_directory)

    assert number_of_grid == 81

