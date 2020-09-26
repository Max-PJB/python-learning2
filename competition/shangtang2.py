n, m = list(map(int, input().split()))


def find_out(gg):
    nn = len(gg)
    mm = len(gg[0])
    x, y, tx, ty = None, None, None, None
    need_keys = set()
    D = {'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e'}
    doors = []
    for i in range(nn):
        for j in range(mm):
            if gg[i][j] == 'S':
                x, y = i, j
            if gg[i][j] == 'X':
                tx, ty = i, j
            if gg[i][j] in D:
                doors.append([i, j])
                need_keys.add(D[gg[i][j]])
    direcs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    dp = [[0 for _ in range(mm)] for _ in range(nn)]
    ac = {(x, y)}
    have_keys = set()
    while ac:
        cx, cy = ac.pop()
        for dx, dy in direcs:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < nn and 0 <= ny < mm:
                if nx == tx and nx == ty:
                    return 'YES'
                else:
                    if gg[nx][ny] == 'X' or gg[nx][ny] in D:
                        pass
                    else:
                        if dp[nx][ny] == 1:
                            pass
                        else:
                            if gg[nx][ny] in need_keys:
                                have_keys.add(gg[nx][ny])
                                if have_keys == need_keys:
                                    for i, j in doors:
                                        gg[i][j] = '.'
                                    for i in range(nn):
                                        for j in range(mm):
                                            dp[i][j] = 0
                            if gg[nx][ny] == 1:
                                pass
                            else:
                                gg[nx][ny] = 1
                                ac.add((nx, ny))
    return 'NO'

while n + m != 0:
    print(n, m)
    grid = []
    input_str = input()
    while len(input_str.split()) == 1:
        grid.append(list(input_str))
        input_str = input()
    print(find_out(grid))
    n, m = list(map(int, input_str.split()))
print(n, m)
"""
7 20
......G..X...dX.X...
.b.......bXX.X..Xb.D
dX.X.....X.aXe..c...
X...D..XX..X..D....c
a..X.Xc.c..bXDXac...
.......C..X.X.c...Xb
b.....eXA..SA..X.dX.
15 11
Xd...E.XaE.
D.E..X..DXB
..A.E...DBb
DX.X..DX.ED
..XX.DXAc..
..XE.X..X.X
c...B...X.B
.X.DX..Xa.b
GcXE.B....B
..A..A..Xea
BX.EdEa..ab
e..XSE.B...
.XA...X.X.C
Cc.X..XeBcb
CXXCC...bX.
0 0
"""
