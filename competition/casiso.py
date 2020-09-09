# [2,3,1,1,4] true
# [3,2,1,0,4] false
a = list(input())
a = list(map(int, a[1::2]))
# print(a)
des = len(a) - 1
start = 0
stack = [0]
reached = {0}
res = False
while stack:
    # print(reached)
    if des in reached:
        res = True
        break
    pos = stack.pop()
    jump = a[pos]
    for j in range(1, jump + 1):
        n_p = pos + j
        if n_p <= des and n_p not in reached:
            # print('pos, j, n_p', pos, j, n_p)
            stack.append(n_p)
            reached.add(n_p)
print(res)
