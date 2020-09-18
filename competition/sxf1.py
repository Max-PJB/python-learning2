T = int(input())
for _ in range(T):
    A, B, N = list(map(int, input().split()))
    cs = list(map(int, input().split()))
    res = [1 for i in range(N)]
    flag = 'NO'
    for i in range(N):
        for j in range(i + 1, N):
            if cs[j] - cs[i] < A:
                res[i] += 1
        if res[i] >= B:
            flag = 'YES'
            break
    print(flag)
