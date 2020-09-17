grid = []
flag = True
t = None
while flag:
    ip = input().split(',')
    if len(ip) > 1:
        grid.append(ip)
    else:
        t = ip[0]
        flag = False
direcs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
starts = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == t[0]:
            starts.append((i, j))
res = False


def dfs(i, j, k, visited):
    global res
    for x, y in direcs:
        ni, nj = i + x, j + y
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[ni]) and (ni, nj) not in visited:
            if grid[ni][nj] == t[k + 1]:
                if k + 1 == len(t) - 1:
                    res = True
                else:
                    dfs(ni, nj, k + 1, visited + [(ni, nj)])


for a, b in starts:
    dfs(a, b, 0, [])
print(res)
