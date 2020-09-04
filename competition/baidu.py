# n = int(input())
# res = [[10 ** 9 for j in range(n)] for _ in range(n)]
# res[0][0] = 0
# scores = []
# for _ in range(n):
# 	scores.append(list(map(int, input().split())))
# direcs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
# d4_scores = [[[] for _ in range(n)] for _ in range(n)]
# for i in range(n):
# 	for j in range(n):
# 		for dirc in direcs:
# 			n_x, n_y = i + dirc[0], j + dirc[1]
# 			if 0 <= n_x < n and 0 <= n_y < n:
# 				d4_scores[i][j].append((n_x, n_y, abs(scores[i][j] - scores[n_x][n_y])))
# 			else:
# 				d4_scores[i][j].append((None, None, None))
# que = {(0, 0)}
# while que:
# 	x, y = que.pop()
# 	for n_x, n_y, s in d4_scores[x][y]:
# 		if s is not None:
# 			n_s = res[x][y] + s
# 			if n_s < res[n_x][n_y]:
# 				res[n_x][n_y] = n_s
# 				que.add((n_x, n_y))
# print(res[n - 1][n - 1])
# # print(res)

n, m, k = list(map(int, input().split()))
gifts = []
for _ in range(n):
	gifts.append(list(map(int, input().split())))
gifts.sort(key=lambda x: [x[2], x[0], x[1]])
res = 0
i = 0
while i < n:
	p, w, _ = gifts[i]
	i += 1
	if k >= p and m >= w:
		res += 1
		k -= p
		m -= w
print(res)
