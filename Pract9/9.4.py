from PIL import Image, ImageDraw, ImageFont

img = Image.open("cat.jpg").convert("RGBA")
txt = Image.new('RGBA', img.size, (255, 255, 255, 0))
draw = ImageDraw.Draw(txt)
try:
    font = ImageFont.truetype("arial.ttf", 24)
except IOError:
    font = ImageFont.load_default()
    
w,h = img.size
draw.text((w//2,h//2), "Watermark", fill=(255, 255, 255, 128), font=font)
wat = Image.alpha_composite(img, txt)
wat = wat.convert("RGB")
wat.save("watcat.jpg")
