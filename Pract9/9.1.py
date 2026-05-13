from PIL import Image

im = "cat.jpg"

try:
    img = Image.open(im)
    print("Размер: ",img.size)
    print("Формат: ",img.format)
    print("Цветовая модель: ",img.mode)
    img.show()
except FileNotFoundError:
    print("картинки нет")
