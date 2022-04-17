import cv2
import numpy as np

pic_path = r'photo/sign_mxp.png'

img = cv2.imread(pic_path)
# 把图片转为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 展示灰度图
# cv2.imshow('gray image', gray)
print(gray)
print(gray.shape)
# t = 12
# # img[img<t] = 0
# # img[img>=t] = 255
# gray = np.where(gray < 120, 0, 255).astype(np.uint8)
_, gray = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)  # https://blog.csdn.net/weixin_42272768/article/details/110746790

# result = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
B = G = R = gray
_, A = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)
result = cv2.merge([B, G, R, A])  # 通道合并
cv2.imshow('result', result)

#
# B2, G2, R2, A2 = cv2.split(result)
# A2 = Alpha
# result = cv2.merge([B2, G2, R2, A2])  # 通道合并
#
cv2.imwrite(r'photo/signature_result.png', result)
# print(result.shape)
# cv2.imshow('result', result)
# B, G, R, A = cv2.split(result)
# cv2.imshow('B', B)
# cv2.imshow('G', G)
# cv2.imshow('R', R)
# cv2.imshow('A', A)

# print(img.dtype)
# print(img.shape)
# cv2.imshow('signature', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
