#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------

    @   Author  :       pengjb
    @   date    :       2021/3/12
    @   IDE     :       PyCharm
    @   GitHub  :       https://github.com/JackyPJB
    @   Contact :       pengjianbiao@hotmail.com
-------------------------------------------------
    Description :       
-------------------------------------------------
"""
import torch
import torch.nn as nn

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


class MyMul(nn.Module):
    def forward(self, input):
        out = input * 2
        return out


class MyMean(nn.Module):  # 自定义除法module
    def forward(self, input):
        out = input / 4
        return out


def tensor_hook(grad):
    print('tensor hook')
    print('grad:', grad)
    return grad


class MyNet(nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()
        self.f1 = nn.Linear(4, 1, bias=True)
        self.f2 = MyMean()
        self.weight_init()

    def forward(self, input):
        self.input = input
        output = self.f1(input)  # 先进行运算1，后进行运算2  8(x1+x2+x3+x4)+2
        output = self.f2(output)  # o = mean(0)
        return output  # 2(x1+x2+x3+x4)+0.25

    def weight_init(self):
        self.f1.weight.data.fill_(8.0)  # 这里设置Linear的权重为8
        self.f1.bias.data.fill_(2.0)  # 这里设置Linear的bias为2

    def my_hook(self, module, grad_input, grad_output):
        print('doing my_hook')
        print('original grad:', grad_input)
        print('original outgrad:', grad_output)
        # grad_input = grad_input[0]*self.input   # 这里把hook函数内对grad_input的操作进行了注释，
        # grad_input = tuple([grad_input])        # 返回的grad_input必须是tuple，所以我们进行了tuple包装。
        # print('now grad:', grad_input)

        return grad_input


if __name__ == '__main__':

    input = torch.tensor([1, 2, 3, 4], dtype=torch.float32, requires_grad=True).to(device)

    net = MyNet()
    net.to(device)

    net.register_backward_hook(net.my_hook)  # 这两个hook函数一定要result = net(input)执行前执行，因为hook函数实在forward的时候进行绑定的
    input.register_hook(tensor_hook)
    result = net(input)

    print('result =', result)

    result.backward()

    print('input.grad:', input.grad)
    for param in net.parameters():
        print('{}:grad->{}'.format(param, param.grad))


x = torch.ones(1, requires_grad=True)
y = x + 2
x.retain_grad()
y.retain_grad()
z = y * y * 3
z.retain_grad()
out = z.mean()
out.retain_grad()
out.backward()
print(x.grad)
print(y.grad)
print(z.grad)
print(out.grad)
# dz = 1
# dy = dz * 3y^2 = 6y = 6(x+2) = 18
# dx = dy * 1 = 18
# z=

