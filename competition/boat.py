#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/19 
    @   IDE     :       PyCharm
    @   Site    :       
-------------------------------------------------
"""
__author__ = 'Max_Pengjb'

a = [[0, 0, 0, 0, 0],
     [0, 1, 0, 1, 0],
     [0, 0, 0, 1, 0],
     [0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0],
     [0, 1, 1, 1, 0],
     [0, 0, 0, 0, 0],
     [0, 1, 0, 1, 0],
     [0, 0, 0, 1, 0],
     [0, 1, 0, 1, 0],
     [0, 1, 0, 0, 1]]
num = 0
for i in range(1, len(a)):
    for j in range(1, len(a[0])):
        if a[i][j] == 1 and a[i-1][j] != 1 and a[i][j-1] != 1:
            num += 1

print("一起有 {} 艘船".format(num))