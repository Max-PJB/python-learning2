t = int(input())

for _ in range(t):
    n = int(input())
    ps = list(map(float, input().split()))
    qs = list(map(float, input().split()))
    i = n - 1
    j = n - 1
    flag = True
    while j >= 0 and flag:
        while i >= 0 and ps[i] != qs[j]:
            i -= 1
        if i < 0:
            flag = False
        j -= 1
    if flag:
        print('YES')
    else:
        print('NO')
