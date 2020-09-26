n, m, r = list(map(float, input().split()))


def step(a, b):
    print('a, b:', a, b)
    if b == 0 and a < n:
        # step down
        x = min(a + r, n)
        y = max(a + r - n, 0)
        return x, y
    elif b < n and a == n:
        # step right
        y = min(b + r, n)
        x = n - max(0, b + r - n)
        return x, y
    elif b == n and a > 0:
        # step up
        x = max(0, a - r)
        y = n - max(0, r - a)
        return x, y
    elif b > 0 and a == 0:
        # step left
        y = max(0, b - r)
        x = max(0, r - b)
        return x, y


xx, yy = 0.0, 0.0
for _ in range(int(m)):
    xx, yy = step(xx, yy)
    print(xx, yy)
