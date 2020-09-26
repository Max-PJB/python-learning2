#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengjb
    @   date    :       2020/9/24 下午3:22
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import cv2

cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(fps, size)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
videoWriter = cv2.VideoWriter('demo_video.mp4', fourcc, fps, size)
while True:
    a, frame = cap.read()
    print(a)
    cv2.imshow("track", frame)
    cv2.imwrite('capture.png',frame)
    videoWriter.write(frame)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
    # break
videoWriter.release()
cv2.destroyAllWindows()
