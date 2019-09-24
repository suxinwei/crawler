# -*- coding:utf-8 -*-
from time import sleep

import tesserocr
from PIL import Image

# image = Image.open('ocr_image.png')

# image = image.convert('1')
threshold = 180
for t in range(180, 181):
    image = Image.open('ocr_image2.jpg')
    image = image.convert('L')
    table = []
    for i in range(256):
        if i < t:
            table.append(0)
        else:
            table.append(1)
    image = image.point(table, '1')
    image.show()
    text = tesserocr.image_to_text(image)
    # sleep(1)
    print('第%d次识别：%s' % (t, text))
    if text == 'dfgu':
        print('成功识别：' + text)
