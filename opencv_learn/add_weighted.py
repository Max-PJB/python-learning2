#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengjb
    @   date    :       2020/9/24 下午5:15
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import cv2
import numpy as np

img = cv2.imread('1.jpg')
print(img.dtype)
img2 = np.zeros(img.shape,dtype=np.uint8) # np.zeros generate data with dtype = float , convert it to unit8
print(img2.dtype)
img3 = cv2.addWeighted(img, 0.5, img2, 0.5, 0.)
cv2.imshow('img1', img)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()
