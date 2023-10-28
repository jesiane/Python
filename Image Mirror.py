from PIL import Image

Image.open('groot.jpg') #original image

img = Image.open('groot.jpg')
Mirror_Image=img.transpose(Image.FLIP_LEFT_RIGHT)
Mirror_Image.save(r'groot_mirror.png')
Image.open('groot_mirror.png')

#pip install pillow