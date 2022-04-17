# -*- coding: utf-8 -*-
import cv2
import base64
import numpy as np


# 图片转base64
def pic_to_b64(pic_path):
    with open(pic_path, "rb") as f:
        # b64encode是编码，b64decode是解码
        base64_data = base64.b64encode(f.read())
    b64_str = base64.b64decode(base64_data)
    return base64_data, b64_str


# base64转为opencv的mat格式
def b64_to_cvmat(b64_str):
    img_data = base64.b64decode(b64_str)
    nparr = np.frombuffer(img_data, np.uint8)
    img_np = cv2.imdecode(nparr,
                          cv2.IMREAD_UNCHANGED)  # cv2.IMREAD_COLOR：默认参数，读入一副彩色图片，忽略alpha通道cv2.IMREAD_GRAYSCALE：读入灰度图片cv2.IMREAD_UNCHANGED：顾名思义，读入完整图片，包括alpha通道
    # cv2.imshow("test",img_np)
    # cv2.waitkey(0)
    return img_np


# 将opencv的mat格式转为base64
def cvmat_to_b64(img_np):
    image = cv2.imencode('.png', img_np)[1]
    base64_data = str((base64.b64encode(image))[2:-1])
    return base64_data


# base64转为图片
def b64_to_pic(b64_str, pic_path):
    # str = "ivborw0kggoaaaansuheugaaanwaaaaocaiaaaaaowpzaaaaaxnsr0iars4c6qaaaarnqu1baacxjwv8yquaaaajcehzcwaadsmaaa7dacdvqgqaaaqusurbvhhe7zptmomgdir7rh6o5+lpvewp01xugshaokgx+8z+7pkrtf6son7e/kmcnslw68wemkmf3ossehsnakhsliq0ifcsge4uijtdhyqgeuoy0j0chlk7knagqkkguloauhyxehpekmladwpcg8rhcrv/hkn3stigw4f88dyox89nobjmanuoc0emxphhcyx9+mowhghkmdlchm0bzzvzet6dssw7xjewk8hu+/o1x7zf1237/uu4t/o46v6szuarozb9kqbo7on4rjlykqcyynnajsbx3gmrj6wtzxirvla+90f82g+nm4fx3zoxgqykqrauu7b8fprdoeyjja7k5obyt1ywse4mxfdc3nrrprnqtqeumuuxourmcghdkfl/ots8melxu2mudo0bxuczl8efvgu0emsqjkgpm2h8y/cwgtw1c3el8ywxhhkwxgolapnj0vcrrw+ooikvcxf0o6yexwlqdanqymf1clhsi22d9hunxobcvzamabmio5bxrdrqot3m3ofuad4/hdolschx7avxzrijqtgsufmu6hb+hglnlc5d5kiwpcaqth7idk/lvld9z0rux4vywl2uj4wy6xbdl91ml57+ejsrnemnw/lcrkkln9nnkbulvksdabjm/zmbyh+pdwuuw6kdeyxpzesfzgarlng1m1enrcfglluuj5mvtg+uyxgzc+1+kn/dkdyutsvbqo7vnnagfkptrh9b8pqtgq/prcifdtaujaiww8aduyckllrcppkyczfkj5cylsznqtkmsyf58oyalmpg6jnlhylc9uxhidwvbr1ns8ahc9pgqlkkai3foorvuk4jgeytjigvtm+mncqrmsfogdj0mololhcmclk3m0kmpzef0mndgvb6ljqbmkb8p5grq34dstrcdpepp5mrnwrnocwsjk9i7nyqugzpytwuszuqe0qvucat5tgh9itmxedcdihjpccvagfi8uj4pgx3k3uhgberq9dtbjmjp1tnymskosh1ugqke23mxlrsri4yksuafnz5braugypw0/idsvhmxhjbei6lrezj0asuoc7tr8bondd9pnkco4lrny9cdgcexjqobdhqvsfpy7z7dsqhp9khxp9dznekbsr+iy3/n31tqvfye17xfuzktu507+4px4usfwbrm32lbzfyxphgrmtn3cwqqaef8a0urmhlajym8rc1iq2deoxvkudvjalmzromst8+4n+egm9rrwzl/dpavlddne9su36jyx6ectkuxufaumjozfwqsxldubntlyo/ckccnss112ydmkkgf/4xkl8rhndrowchbkmrv61qgfbwimepbrqglg105aovchdkcve4ty0chlknrly1qgfcwseep7zrgfc20zwrvihakcve49q2chdknrpy1qof/gdxihmwmc+csaaaaabjru5erkjggg=="
    img_data = base64.b64decode(b64_str)
    with open(pic_path, "wb") as f:
        f.write(img_data)
    return img_data


def b64_to_pic_with_opencv(b64_str, pic_path):
    img_np = b64_to_cvmat(b64_str)
    cv2.imwrite(pic_path, img_np)


if __name__ == '__main__':
    pic_path = r'photo/sign_mxp.png'
    b64_byte_str, b64_byte_0x = pic_to_b64(pic_path)
    print(b64_byte_str)
    print(b64_byte_0x)
    pic = b64_to_pic(b64_byte_str, r'photo/haha.jpg')
    b64_to_pic_with_opencv(b64_byte_str, r'photo/haha2.png')
    pic_np = b64_to_cvmat(b64_byte_str)
    cv2.imshow('b64_to_cvmat', pic_np)
    cv2.waitKey()
    cv2.destroyAllWindows()
    from flask import Flask, jsonify
    from flask_cors import CORS

    # from flask_web.app import jsonReturn

    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})


    @app.route('/img_b64/<img_id>', methods=['GET'])
    def get_img_b64_by_id(img_id):
        print(img_id)
        return jsonify({
            "status": "failed",
            "code": "500",
            # imageDataUrl = 'data:image/png;base64,' + Imgbase
            "data": f'data:image/png;base64,{str(b64_byte_str, encoding="utf - 8")}',
            "msg": 2,
        })


    app.run()
