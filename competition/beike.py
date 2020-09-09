t = int(input())


def score(a, b):
    if a == 'S' and b == 'J':
        return 1
    elif a == 'J' and b == 'B':
        return 1
    elif a == 'B' and b == 'S':
        return 1
    else:
        return 0


for _ in range(t):
    a1, a2, b1, b2 = input().split()
    r_left = score(a1, b1) + score(a1, b2)
    r_right = score(a2, b1) + score(a2, b2)
    print(r_left, r_right)
    if r_left > r_right:
        print('left')
    elif r_left == r_right:
        print('same')
    else:
        print('right')


# n = int(input())
# target = input()
# k = n // 2
# """
# 9
# ababababc
# = 6
# """
# res = n
# for i in range(k, 0, -1):
#     # print(target[:i], target[:2 * i])
#     if target[:i] * 2 == target[:2 * i]:
#         res = n - i + 1
#         break
# print(res)

# t = int(input())
# M = 10 ** 9 + 7
# for _ in range(t):
#     n, m = list(map(int, input().split()))
#     res = m
#     while n > 1:
#         res = res * (m - 1) % M
#         n -= 1
#     print(res)
#
