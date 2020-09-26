#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengjb
    @   date    :       2020/9/24 下午10:34
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import cv2
import numpy as np

img2 = cv2.imread('capture.png')
arrow_img = cv2.imread('right.png')


def paint_arrow(alpha_l, alpha_r, img, arrow):
    h, w, _ = arrow.shape
    red = np.array([[255 - i, 255 - i, i] for i in np.linspace(150, 255, w)])
    color_r = int(w * alpha_r)
    color_l = int(w * alpha_l)
    arrow_r = arrow.copy()
    arrow_r[5:h - 5, 5:color_r] = red[5:color_r]
    arrow_l = arrow.copy()
    arrow_l[5:h - 5, 5:color_l] = red[5:color_r]
    arrow_l = arrow_l[:, ::-1]

    img_h, img_w, _ = img.shape
    h_gap = 20
    w_gap = 30
    img[h_gap:h_gap + h, w_gap:w_gap + w] = np.where(arrow_l > 0, arrow_l, img[h_gap:h_gap + h, w_gap:w_gap + w])
    img[h_gap:h_gap + h, img_w - w_gap - w:img_w - w_gap] = np.where(arrow_r > 0, arrow_r, img[h_gap:h_gap + h,
                                                                                           img_w - w_gap - w:img_w - w_gap])


paint_arrow(.5, .5, img2, arrow_img)
cv2.imshow('img2', img2)
cv2.waitKey()
cv2.destroyAllWindows()
