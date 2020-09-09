s = input()


def conv2num(c):
    n = ord(c)
    if 97 <= n <= 122:
        return n - 96
    elif 65 <= n <= 90:
        return n - 38
    elif 48 <= n <= 57:
        return n + 5
    else:
        return 0


num_str = ''

for i in range(len(s)):
    num_str += (bin(conv2num(s[i])))[2:].zfill(6)
for i in range(0, len(num_str), 30):
    num = num_str[i:i + 30]
    print(int(num, 2), end=' ')

# Aa0Z9a
# 453467454 1