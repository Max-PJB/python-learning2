n, m = list(map(int, input().split()))
q = [[i] for i in range(n + 1)]
d = {i: (i, 1) for i in range(1, n + 1)}
for _ in range(m):
    op, a, b = list(input().split())
    a = int(a)
    b = int(b)
    if op == 'C':
        if a != b:
            for x in q[a]:
                q[b].append(x)
                d[x] = (b, len(q[b]))
            q[a] = []
    else:
        if d[a][0] == d[b][0]:
            print(abs(d[a][1] - d[b][1]) - 1)
        else:
            print(-1)
    print(q, d)

"""
6 6
C 3 6
C 4 1
Q 1 6
C 1 6
Q 1 6
Q 2 5
"""
