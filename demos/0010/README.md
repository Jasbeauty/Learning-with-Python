### 使用 Python 生成类似于下图中的字母验证码图片
```
import random, string
from PIL import Image, ImageDraw, ImageFont, ImageFilter


# 获得随机四个字母
def get_code():
    chars = string.ascii_letters
    return random.choice(chars)


# 获得随机颜色1（像素点）
def random_color1():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


# 获得随机颜色2（随机字母）
def random_color2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


def compose():
    width = 240
    height = 60
    img = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('SantasSleighFull.ttf', 45)
    draw = ImageDraw.Draw(img)
    # 填充每个像素
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=random_color1())

    # 输出文字
    code = []
    for i in range(4):
        code.append(get_code())
        draw.text((60 * i + 10, 10), code[i], font=font, fill=random_color2())

    img.save('code.jpg', 'jpeg')
    # 图像模糊
    img1 = img.filter(ImageFilter.BLUR)
    img1.save('filter.jpg', 'jpeg')


if __name__ == '__main__':
    compose()
```

#### 演示
![](code.png)


![](blur.png)

