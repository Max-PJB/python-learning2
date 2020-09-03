#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       Max_Pengjb
    @   date    :       2018/9/22 19:38
    @   IDE     :       PyCharm
    @   Site    :       
-------------------------------------------------
    Description :       
-------------------------------------------------
"""

__author__ = 'Max_Pengjb'


def x(f):
    def y():
        print(1)

    return y


def f():
    print(2)


x(f)  # 啥也不干
x(f())  # 打印 2
x(f())()  # 打印 2  和 1   x(f()) -> x(f) return y -> y()
