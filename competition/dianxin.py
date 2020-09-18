def n_ugly2(k):
    if k == 1:
        return 1
    uglies = [1]
    p2 = 0
    p3 = 0
    p5 = 0
    for _ in range(k - 1):
        next_ugly = min(uglies[p2] * 2, uglies[p3] * 3, uglies[p5] * 5)
        if next_ugly == uglies[p2] * 2:
            p2 += 1
        if next_ugly == uglies[p3] * 3:
            p3 += 1
        if next_ugly == uglies[p5] * 5:
            p5 += 1
        uglies.append(next_ugly)
    return uglies[-1]


def is_ugly(x):
    while x % 2 == 0:
        x //= 2
    while x % 3 == 0:
        x //= 3
    while x % 5 == 0:
        x //= 5
    if x == 1:
        return True
    else:
        return False


def n_ugly1(k):
    i = 1
    cnt = 1
    while cnt < k:
        i += 1
        while not is_ugly(i):
            i += 1
        cnt += 1
    return i


n = 1500
for z in range(1, n):
    print(n_ugly2(z))
