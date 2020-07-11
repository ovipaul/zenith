# Improting Image class from PIL module 
from PIL import Image 
import numpy as np
# Opens a image in RGB mode 

def overlap_grid(img_file,overlap_percentage,output_dir, init_exclude):
    file_name = img_file.rstrip('.png')
    file_name = file_name[init_exclude:]
    print(file_name)
    img = Image.open(img_file) 
    

    cal_img = np.array(img)
    row, col, cha = cal_img.shape

    img_width = 513
    img_height = 513

    overlap = int((img_width*overlap_percentage)/100)
    # Setting the points for cropped image 
    print(overlap)

    top = 0    
    bottom = img_height


    counter = 0

    for i in range(row):
        if (row-bottom) < img_height :
            break
        #initial vs other time values
        if i is not 0:
            top = top+overlap
            bottom = bottom+overlap

        left = 0
        right = img_width
        
        for j in range(col):
            if (col-right) < img_width :
                break
            if j is not 0:
                left = left+overlap
                right = right+overlap

            

            final_img = img.crop((left, top, right, bottom)) 

            # Shows the image in image viewer 
            final_img.save(output_dir+'/'+file_name+'_'+str(counter)+'.png')
            counter = counter + 1
