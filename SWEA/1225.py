#1225 D3


n = 10
for i in range(n):
    tc = int(input())
    code = list(map(int, input().split()))
    cycle = 0
    i = 1
    while True:
        if i > 5:
            i = 1
        t = code.pop(0) - i
        if t <= 0:
            code.append(0)
            break
        code.append(t)
        i += 1
    print(f'#{tc}', end=' ')
    print(*code)
