# n, *link = list(map(int, input().split()))
# res = []
#
#
def hebing(link1, link2):
    i, j = 0, 0
    r = []
    while i < len(link1) and j < len(link2):
        k1, v1 = link1[i]
        k2, v2 = link2[j]
        if k1 == k2:
            r.append([k1, v1 + v2])
            i += 1
            j += 1
        elif k1 < k2:
            r.append([k1, v1])
            i += 1
        else:
            r.append([k2, v2])
            j += 1
    if i < len(link1):
        r.extend(link1[i:])
    else:
        r.extend(link2[j:])
    return r


#
#
# for _ in range(n):
#     kvs = input().split()
#     kv = [list(map(int, x.split(':'))) for x in kvs]
#     res = hebing(res, kv)
#     #print(res)
# for k, v in res:
#     print(str(k) + ':' + str(v), end=' ')
n, *link = list(map(int, input().split()))
from collections import defaultdict

links = []
res = defaultdict(int)
for _ in range(n):
    kvs = input().split()
    links.append([list(map(int, x.split(':'))) for x in kvs])
while len(links) > 1:
    n = len(links)
    t = []
    for i in range(0, n, 2):
        if i + 1 < n:
            t.append(hebing(links[i], links[i + 1]))
        else:
            t.append(links[i])
    links = t
res = links[0]
for k, v in res:
    print(str(k) + ':' + str(v), end=' ')