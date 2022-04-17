#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengjb
    @   date    :       2020/9/22 下午10:54
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :
-------------------------------------------------
"""
import requests
import base64
import json

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication
# from PIL import Image
import datetime


# 将文件转换为base64编码，上传文件必须将文件以base64格式上传
def read_file_base64(file_path):
    # 读取文件
    with open(file_path, 'rb') as f:
        data = f.read()
    data_b64 = base64.b64encode(data).decode('utf-8')
    return data_b64


# 上传文件
def upload_file(image_base64):
    # dt_ms = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')  # 含微秒的日期时间
    dt_ms = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')  # 含微秒的日期时间
    image_name = 'image-' + dt_ms + '.png'  # 文件名
    token = "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"  # 当前的 token 已经失效，使用的话需要重新申请
    url = "https://api.github.com/repos/max-pjb/imgs/contents/" + image_name  # 用户名、库名、路径
    headers = {"Authorization": "token " + token}
    data = {
        "message": "uploaded by custom script",
        "committer": {
            "name": "pengjb",
            "email": "pengjianbiao@hotmail.com"
        },
        "content": image_base64
    }
    data = json.dumps(data)
    req = requests.put(url=url, data=data, headers=headers)
    req.encoding = "utf-8"
    re_data = json.loads(req.text)
    # print(re_data)
    # print(re_data['content']['sha'])
    print("https://cdn.jsdelivr.net/gh/max-pjb/imgs/" + image_name)


# 在国内默认的down_url可能会无法访问，因此使用CDN访问


if __name__ == '__main__':
    # import sys
    #
    # png_path = sys.argv[1]
    # with open(png_path, 'rb') as f:
    #     img_b64 = base64.b64encode(f.read()).decode('utf-8')
    # upload_file(img_b64)
    app = QApplication([])
    cb = app.clipboard()
    print(cb.mimeData().hasText())
    if cb.mimeData().hasImage():
        print('haha')
        qt_img = cb.image()
        # print(type(qt_img))
        # Qimage to base64
        # QImage通过ByteArray转化为BASE64字符串
        qb = QtCore.QByteArray()
        buf = QtCore.QBuffer(qb)
        qt_img.save(buf, 'PNG')
        img_b64 = base64.b64encode(qb).decode('utf-8')
        # pil_img = Image.fromqimage(qt_img)  # 转换为PIL图像
        # pil_img.save('./haha.png', "PNG")
        upload_file(img_b64)
