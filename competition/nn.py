xs = list(map(int, input().split()))
ys = list(map(int, input().split()))
xs.sort()
ys.sort()
i, j = 0, 0
res = 0
while i < len(xs) and j < len(ys):
    x = xs[i]
    y = ys[j]
    if x <= y:
        res += 1
        i += 1
        j += 1
    else:
        j += 1
print(res)
import bisect

xm = xs[-1]
ym = ys[-1]
print(min(bisect.bisect_right(xs, ym), bisect.bisect_right(ys, xm)))
