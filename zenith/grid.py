# Improting Image class from PIL module 
from PIL import Image 
import numpy as np
# Opens a image in RGB mode 

def grid(img_file,img_width,img_height,overlap_percentage,output_directory):
    overlap_percentage = 100-overlap_percentage
    file_name = img_file.rstrip('.png')


    img = Image.open(img_file) 
    

    cal_img = np.array(img)
    row, col, cha = cal_img.shape


    overlap = int((img_width*overlap_percentage)/100)
    # Setting the points for cropped image 

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


            final_img.save(output_directory+'/'+file_name+'_'+str(counter)+'.png')
            counter = counter + 1