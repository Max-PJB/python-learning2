# N, a, b, c, d = list(map(int, input().split()))
#
#
# def jc(x):
# 	r = 1
# 	for i in range(1, x + 1):
# 		r *= i
# 	return r
#
# res = int(jc(N * N) / (jc(a) * jc(b) * jc(c) * jc(d))) %
# print(res)
from collections import defaultdict

n = int(input())

edges = defaultdict(list)
for _ in range(n - 1):
    u, v = list(map(int, input().split()))
    edges[u].append(v)


def subtree(k):
    if edges[k]:
        return max(list(map(subtree, edges[k]))) + len(edges[k]) - 1
    else:
        return 0


print(subtree(1))
