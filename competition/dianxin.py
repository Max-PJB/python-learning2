def n_ugly(k):
    if k == 1:
        return 1
    uglies = [1]
    p2 = 0
    p3 = 0
    p5 = 0
    for _ in range(k-1):
        next_ugly = min(uglies[p2] * 2, uglies[p3] * 3, uglies[p5] * 5)
        if next_ugly == uglies[p2] * 2:
            p2 += 1
        if next_ugly == uglies[p3] * 3:
            p3 += 1
        if next_ugly == uglies[p5] * 5:
            p5 += 1
        uglies.append(next_ugly)
    return uglies[-1]


print(n_ugly(10))