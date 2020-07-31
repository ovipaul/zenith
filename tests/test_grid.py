from PIL import Image
from zenith.grid import grid

Image.MAX_IMAGE_PIXELS = 350000000000000

def test_grid():

    overlap_percentage = 50
    img_dim = 250
    file_name = 'test_image.png'
    print(file_name)
    number_of_grid = grid(file_name, img_dim, overlap_percentage)

    assert number_of_grid == 81

