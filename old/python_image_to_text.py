#from PIL import Image
#import PIL.Image



#use Pillow instead of PIL
from PIL import Image
im = Image.open("IMAGE1.JPG")
#im.show()

from pytesseract import image_to_string
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
output = pytesseract.image_to_string(im.convert("RGB"), lang='eng')
print(output)
