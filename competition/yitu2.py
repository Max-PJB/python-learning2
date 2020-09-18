t = int(input())


def gg(n, m, grid, x, y, a, b, c, d):
    direcs = [(-1, 0, a), (1, 0, b), (0, -1, c), (0, 1, d)]
    dp = [[10 ** 9 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 0
    q = {(0, 0)}
    while q:
        cx, cy = q.pop()
        for dx, dy, cost in direcs:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != 'x':
                ncost = dp[cx][cy] + cost
                if ncost < dp[nx][ny]:
                    dp[nx][ny] = ncost
                    q.add((nx, ny))
    for p in dp:
        print(p)
    if dp[x][y] == 10 ** 9:
        return -1
    else:
        return dp[x][y]


for i in range(t):
    n, m = list(map(int, input().split()))
    x, y = list(map(int, input().split()))
    a, b, c, d = list(map(int, input().split()))
    grid = []
    for _ in range(n):
        grid.append(list(input()))
    print('Case #' + str(i + 1) + ':', gg(n, m, grid, x, y, a, b, c, d))

"""
2
5 5
2 2 
1 5 25 125
ooooo
oxxxo
oxooo
oxxxo
ooooo
5 5
2 2 
0 0 0 0
ooooo
oxxxo
oxoxo
oxxxo
ooooo[0, 125, 250, 375, 500]
[5, 1000000000, 1000000000, 1000000000, 505]
[10, 1000000000, 560, 535, 510]
[15, 1000000000, 1000000000, 1000000000, 515]
[20, 145, 270, 395, 520]
Case #1: 560

[0, 0, 0, 0, 0]
[0, 1000000000, 1000000000, 1000000000, 0]
[0, 1000000000, 1000000000, 1000000000, 0]
[0, 1000000000, 1000000000, 1000000000, 0]
[0, 0, 0, 0, 0]
Case #2: -1
"""