from collections import defaultdict

ss = input()
s_d = defaultdict(int)
for s in ss:
    s_d[s] += 1
s_s_d = sorted(s_d.items(), key=lambda x: x[1])
min_sd = s_s_d[0][1]
for k, v in s_s_d:
    if v == min_sd:
        s_d.pop(k)
for s in ss:
    if s in s_d:
        print(s, end='')