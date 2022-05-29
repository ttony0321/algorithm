#12368 D3

n = int(input())

for tc in range(n):
    m = 0
    a, b = map(int, input().split())
    m = a
    m += b
    k = 0
    if m > 24:
        k = m - 24
        m = 0
        m += k
    elif m == 24:
        m = 0
    else:
        pass
    print(f'#{tc+1} {m}')

