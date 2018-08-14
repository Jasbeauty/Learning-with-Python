### 将QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果
```
from PIL import Image, ImageDraw, ImageFont


def add_num(picPath, num):
    img = Image.open(picPath)
    x_Size, y_Size = img.size

    # //得到的是int值  /得到的是float值
    font_size = y_Size // 4

    position = x_Size - font_size
    my_font = ImageFont.truetype('Christmas.ttf', font_size)
    ImageDraw.Draw(img).text((position, 0), str(num), font=my_font, fill=(219, 81, 73))
    img.save('icon_with_num.png')


if __name__ == '__main__':
    add_num('icon.jpg', 7)
```

#### 演示
![icon_with_num](icon_with_num.png)
