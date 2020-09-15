n, m = list(map(int, input().split()))
sb = []
xb = []
res = {i for i in range(1, n + 1)}
for _ in range(m):
    ai, bi = list(map(int, input().split()))
    if bi:
        sb.append(ai)
    else:
        xb.append(ai)
res = res - set(sb) - set(xb)
if sb[0] == xb[-1]:
    if set(xb) - set(sb) or set(sb) - set(xb):
        # res = res - set(xb) - set(sb)
        pass
    else:  # set(sb) - set(xb):
        # res = (res - set(sb)) | {sb[0]}
        res.add(sb[0])
else:
    if sb[0] not in xb:
        if not set(xb) - set(sb):
            res.add(sb[0])
    elif xb[-1] not in sb:
        if not set(sb) - set(xb):
            res.add(xb[-1])
res = sorted(list(res))
print(res)

