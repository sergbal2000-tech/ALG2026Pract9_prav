from PIL import Image

im = "cat.jpg"
img = Image.open(im)

size = (img.width // 3, img.height // 3)
simg = img.resize(size)
simg.save("small.jpg")

hflip = img.transpose(Image.FLIP_LEFT_RIGHT)
hflip.save("hflip.jpg")

vflip = img.transpose(Image.FLIP_TOP_BOTTOM)
vflip.save("vflip.jpg")
