from PIL import Image
import PIL.ImageOps

image = Image.open('bw_image.png')

inverted_image = PIL.ImageOps.invert(image)

inverted_image.save('new_name.png')