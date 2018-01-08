import rawpy
import imageio
import os
from PIL import Image
files=[]
files = list(os.listdir())
count=0
for i in files:
    raw = rawpy.imread(i)
    rgb = raw.postprocess()
    imageio.imsave('def'+str(count) +'.tiff', rgb)
    im = Image.open('def'+str(count)+'.tiff')
    im.save('image_'+ str(count) +'.jpeg')
    os.remove('def'+str(count)+'.tiff')
    count=count+1
    if(count==len(files)-1):
        break
