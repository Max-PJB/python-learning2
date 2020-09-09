# def gcd(a, b):
#     while b:
#         _, y = divmod(a, b)
#         a = b
#         b = y
#     return a
#
#
# a = input()
# b = input()
# k = gcd(len(a), len(b))
# if a[:k] * (len(b) // k) == b and a[:k] * (len(a) // k) == a:
#     print(a[:k])
# else:
#     print('')

# n, m = list(map(int, input().split()))
# direc = (-1, 1)
# res = [[None for _ in range(m)] for _ in range(n)]
# cnt = 1
# for i in range(n):
#     x, y = i, 0
#     while 0 <= x < n and 0 <= y < m:
#         res[x][y] = cnt
#         cnt += 1
#         x -= 1
#         y += 1
# for j in range(1, m):
#     x, y = n - 1, j
#     while 0 <= x < n and 0 <= y < m:
#         res[x][y] = cnt
#         cnt += 1
#         x -= 1
#         y += 1
# # for r in res:
# #     print(r)
# # print(','.join(list(map(lambda x: ','.join(x), res))))
# print(res)

a = input()
n = len(a)


def int_to_list(x):
    r = []
    while x:
        r.append(x & 1)
        x >>= 1
    return r[::-1]


def int_to_ord_str(x):
    b = bin(x)
    # print(b)
    c = b[2:]
    # print(c)
    d = '0' * (6 - len(c)) + c
    # print(d)
    return d


res = 0
ch_int_dict = {}
for i in range(26):
    ch_int_dict[chr(ord('a') + i)] = int_to_ord_str(1 + i)
    ch_int_dict[chr(ord('A') + i)] = int_to_ord_str(27 + i)
for i in range(10):
    ch_int_dict[chr(ord('0') + i)] = int_to_ord_str(53 + i)
# print(ch_int_dict,len(ch_int_dict))
for i in range(0, n, 5):
    cs = a[i:i + 5]
    r = [0,0]
    for c in cs:
        pass
print(ord('0'))
print(int_to_list(10))
a = bin(1)
print(type(a),a,a[2:])
print(chr(ord('a') + 2))
