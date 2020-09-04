n, m = list(map(int, input().split()))
scores = []
for _ in range(n):
	scores.append(list(map(int, input().split())))
direcs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

from decimal import Decimal, ROUND_HALF_UP


def cal(x, y):
	tmp = [scores[x][y]]
	for direc in direcs:
		n_x, n_y = x + direc[0], y + direc[1]
		if 0 <= n_x < n and 0 <= n_y < m:
			tmp.append(scores[n_x][n_y])
	return int(Decimal(sum(tmp) / len(tmp)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))


for i in range(n):
	for j in range(m):
		scores[i][j] = cal(i, j)
for ss in scores:
	print(" ".join(list(map(str, ss))))
