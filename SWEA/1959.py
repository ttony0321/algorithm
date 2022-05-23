#1959 D2

n = int(input())

for tc in range(n):
    fn, sn = map(int, input().split())
    fl = list(map(int, input().split()))
    sl = list(map(int, input().split()))

    result = 0

    for i in range(abs(fn - sn)+1):
        v = 0
        for j in range(min(fn, sn)):
            if len(fl) > len(sl):
                v += fl[j+i] * sl[j]
            elif len(fl) < len(sl):
                v += fl[j] * sl[j+i]
            else:
                v += fl[j] * sl[j]
        if v > result:
            result = v
    print(f'#{tc+1} {result}')