def prime_numbers_below2(x):
    vis = [0 for _ in range(x + 1)]
    prime_table = []
    ln = 0
    for num in range(2, x + 1):
        if vis[num] == 0:
            prime_table.append(num)
            ln += 1
        for j in range(ln):
            if num * prime_table[j] > x:
                break
            vis[num * prime_table[j]] = 1
            if num % prime_table[j] == 0:
                break
    return prime_table


n = int(input())
ps = prime_numbers_below2(n)
i = 0
while i < len(ps) and ps[i] <= n:
    if n % ps[i] == 0:
        print(ps[i])
        n //= ps[i]
    else:
        i += 1
