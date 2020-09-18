import math

n = int(input())
max_speed = 0
res = 0
pre = list(map(int, input().split()))

for i in range(1, n):
    cur = list(map(int, input().split()))
    dis = math.sqrt((cur[1] - pre[1]) ** 2 + (cur[2] - pre[2]) ** 2 + (cur[3] - pre[3]) ** 2)
    t = cur[0] - pre[0]
    speed = dis / t
    if max_speed < speed:
        max_speed = speed
        res = i
    pre = cur
print(res)
"""
3
2 -9 2 3
4 9 9 8
9 2 3 4
"""
