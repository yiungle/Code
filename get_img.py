# coding:utf-8
import os
import time
import requests
from PIL import Image
from io import BytesIO


def down_img(img_url, img_path=None, img_name=None):
    """
    :param img_url: 图片下载链接
    :param img_path: 图片下载路径(默认当前路径img下)
    :param img_name: 图片名称(默认当前时间戳)
    :return: 下载路径及名称
    """
    if not img_path:
        img_path = 'img'
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    if not img_name:
        img_type = '.' + img_url.split('.')[-1]
        img_name = str(int(time.time())) + img_type

    image = Image.open(BytesIO(requests.get(img_url).content))
    image.save(os.path.join(img_path, img_name))
    return img_path


if __name__ == '__main__':
    url_list = [
        'http://img.jyeoo.net/quiz/images/201710/251/5ca671c3.png',
        'http://img.jyeoo.net/quiz/images/201708/35/0fdddd9d.png',
        'http://img.jyeoo.net/quiz/images/201710/201/c026891a.png',
        'http://img.jyeoo.net/quiz/images/201710/201/b838f059.png',
        'http://img.jyeoo.net/quiz/images/201710/163/be3625cc.png',
        'http://img.jyeoo.net/quiz/images/201710/145/bf39ca39.png',
        'http://img.jyeoo.net/quiz/images/201710/198/01a510f7.png',
    ]
    for u in url_list:
        url = u
        path = "/".join(url.split("/")[3:-1])
        name = url.split("/")[-1]
        print(down_img(url, path, name))
