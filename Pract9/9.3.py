import os
from PIL import Image, ImageFilter

Dir = "filt"
os.makedirs(Dir, exist_ok=True)

for i in range(1, 6):
    fn = f"{i}.jpg"
    if os.path.exists(fn):
        img = Image.open(fn)
        filtimg = img.filter(ImageFilter.CONTOUR)
        way = os.path.join(Dir, f"filt-{i}.jpg")
        filtimg.save(way)
        print(f"Обработан файл: {fn}")
    else:
        print(f"Файл {fn} не найден")
