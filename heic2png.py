import os
import subprocess
from PIL import Image

dir0 ='org'
dir1 = 'png'
dir2 = 'png_resize'

files0 = os.listdir(dir0)
files0.sort()

for file in files0:

    if '.HEIC'  in file:        
        command = 'sips --setProperty format png ' + dir0 +'/' + file +  ' --out ' + dir1 +'/' +  file.replace('.HEIC','.png') 
        subprocess.call(command, shell=True)
        print(file) 
        
files1 = os.listdir(dir1)
files1.sort()
print('')

for file in files1:
    
    if '.png' in file:   
        img0 = os.path.join(dir1, file)
        img0_img = Image.open(img0)
        img1_img = img0_img.resize((300,300)) 
        img1 = os.path.join(dir2, file) 
        img1_img.save(img1)
        print(file)
    
