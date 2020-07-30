# Improting Image class from PIL module 
from PIL import Image 
import numpy as np
# Opens a image in RGB mode 
import io

def grid(img_file,img_width,img_height,overlap_percentage,output_directory):
    overlap_percentage = 100-overlap_percentage
    file_name = img_file.rstrip('.png')


    img = Image.open(img_file) 
    # with open(img_file, 'rb') as f:
    #     img = Image.open(io.BytesIO(f.read()))

    cal_img = np.array(img)
    rows, cols, cha = cal_img.shape


    overlap = int((img_width*overlap_percentage)/100)
    # Setting the points for cropped image 

    top = 0    
    bottom = img_height


    counter = 0
    #initial coordinate
    row = 0
    col = 0
    for row in range(rows):
        if (rows-bottom) < img_height :
            break
        #initial vs other time values
        if row != 0:
            top = top+overlap
            bottom = bottom+overlap

        left = 0
        right = img_width
        
        for col in range(cols):
            if (cols-right) < img_width :
                break
            if col != 0:
                left = left+overlap
                right = right+overlap

            

            final_img = img.crop((left, top, right, bottom)) 


            final_img.save(output_directory+'/'+file_name+'_'+str(counter)+'.png')
            counter = counter + 1
    return counter
