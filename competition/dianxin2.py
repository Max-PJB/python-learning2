n = int(input())
stack = []

for _ in range(n):
    line = input().split()
    cao_zuo, val = None, None
    if len(line) == 1:
        cao_zuo = line[0]
    else:
        cao_zuo, val = line
        val = int(val)
    if cao_zuo == 'push':
        stack.append(val)
    elif cao_zuo == 'pop':
        if stack:
            stack.pop()
    elif cao_zuo == 'top':
        if stack:
            print(stack[-1])
    elif cao_zuo == 'getMin':
        if stack:
            print(min(stack))
