T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(lambda x: int(x) - 1, input().split()))
    j = 0
    indexes = {0}
    res = 0
    k = len(a)
    while len(indexes) < k:
        j = a[j]
        if j in indexes:
            res += 1
            while j in indexes:
                j = (j + 1) % k
        indexes.add(j)
    print(res + 1)
