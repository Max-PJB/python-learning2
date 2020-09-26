#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengjb
    @   date    :       2020/9/22 下午7:14
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""


#
#
# @param inData string字符串 请求参数
# @return int整型
#
class Solution:
    def sort2(self, inData):
        # write code here
        if len(inData) < 2:
            return 0
        # print(inData)
        cur_min = min(inData)
        ind = inData.index(cur_min)
        pops = inData[:ind]
        left = inData[ind + 1:]
        pop_min = min(pops, default=5000)
        next_left = list(filter(lambda x: x < pop_min, left))
        # print(left,next_left)
        return self.sort2(next_left) + len(pops) + len(left) - len(next_left)

    def sort(self, inData):
        data = list(map(int,inData.split(',')))
        return self.sort2(data)


rr = Solution().sort("19 5 9 255")
print(rr)
