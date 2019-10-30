import os
import time
import requests
from PIL import Image
from io import BytesIO


def down_img(url, path='img', img_name=str(int(time.time()))):
    """
    :param url: 图片下载链接
    :param path: 图片下载路径(默认当前路径img下)
    :param img_name: 图片名称(默认当前时间戳)
    :return: 下载路径及名称
    """
    img_type = '.' + url.split('.')[-1]
    img_path = os.path.join(path, img_name + img_type)
    if not os.path.exists(path):
        os.makedirs(path)
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image.save(img_path)
    return img_path


if __name__ == '__main__':
    down_img(url='http://img.jyeoo.net/quiz/images/201710/251/5ca671c3.png')
