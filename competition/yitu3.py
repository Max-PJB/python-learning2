N, K1, K2 = list(map(int, input().split()))
x, y, z = list(map(int, input().split()))
prods = []
for _ in range(N):
    a, b, c, p = list(map(int, input().split()))
    prods.append((a * 17 * 29 + b * 29 + c, p))
if K2 >= K1:
    print('YES')
    print(x, y, z)
else:
    prods.sort(key=lambda q: q[0])
    m = x * 17 * 29 + y * 29 + z
    dp = [[0 for _ in range(N + 1)] for _ in range(m + 1)]
    flag = True
    res = None
    for money in range(1, m + 1):
        for j in range(1, N):
            cost, p = prods[j - 1]
            if money - cost >= 0:
                dp[money][j] = max(dp[money][j - 1], dp[money - cost][j - 1] + p, dp[money - cost][j])
            else:
                dp[money][j] = dp[money][j - 1]
            if dp[money][j] >= K1 - K2:
                flag = False
                res = money
                break
        if not flag:
            break
    if res is None:
        print('NO')
    else:
        print('YES')
        left = m - res
        a, left = divmod(left, 17 * 29)
        b, left = divmod(left, 29)
        print(a, b, left)
