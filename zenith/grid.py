import os
from PIL import Image
import numpy as np

def grid(img_file, img_dim, overlap_percentage):
    if not os.path.exists('grid_output'):
        os.makedirs('grid_output')

    overlap_percentage = 100-overlap_percentage
    file_name = img_file.rstrip('.png')
    img = Image.open(img_file)

    cal_img = np.array(img)

    rows, cols = cal_img.shape[0:2]

    overlap = int((img_dim*overlap_percentage)/100)#img_width

    # Setting the points for cropped image
    top = 0
    bottom = img_dim #img_height

    counter = 0
    #initial coordinate
    row = 0
    col = 0

    for row in range(rows):
        if(rows-bottom) < img_dim : #img_height
            break
        #initial vs other time values
        if row != 0:
            top = top+overlap
            bottom = bottom+overlap

        left = 0
        right = img_dim     #img_width
        for col in range(cols):
            if(cols-right) < img_dim : #img_width
                break
            if col != 0:
                left = left+overlap
                right = right+overlap

            final_img = img.crop((left, top, right, bottom))
            final_img.save('grid_output'+'/'+file_name+'_'+str(counter)+'.png')
            counter = counter + 1

    return counter
