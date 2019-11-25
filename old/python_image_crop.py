#use Pillow instead of PIL
from PIL import Image
im = Image.open("IMAGE1.PNG")
im.show()

# Setting the points for cropped image 
left = 829
top = 509
right = 1091
bottom = 641
  
# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 

im1.show()