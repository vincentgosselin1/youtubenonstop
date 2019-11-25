#python_printscreen_to_messagebox_text.py
#Vincent Gosselin, 2019.

#use Pillow instead of PIL
from PIL import Image
import PIL.ImageGrab
import pytesseract
from pytesseract import image_to_string
import time

#Printscreen
im = PIL.ImageGrab.grab()
#im.show()

#Test image.
#im = Image.open("IMAGE1.PNG")
#im.show()

# Setting the points for cropped image 
left = 829
top = 509
right = 1091
bottom = 641
  
# Cropped image of above dimension 
# (It will not change orginal image) 
im1 = im.crop((left, top, right, bottom)) 

#im1.show()

print("jean1")
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
print("jean2")
output = pytesseract.image_to_string(im1.convert("RGB"), lang='eng')
print("jean3")
#output = pytesseract.image_to_string(im, lang='eng')
print(output)
str = output
print(str)


#If output inclues "Video paused. Continue watching?"
ret = str.find("Video paused")
#ret is -1 if it doesnt find string
#ret is 0 if it finds it!
if ret == 0:
	print("its there!!!")
	#This is where I need to generate a left mouse click.
	
	#CLICKKKKKK
	print('Click!!!!\n')
	pyautogui.click(300, 300)
	
	#show cropped image
	im1.show()
	
else:
	print("its NOT there!!!")











