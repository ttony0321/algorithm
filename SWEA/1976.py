#1976 D2

n = int(input())


for tc in range(n):
    h = 0
    m = 0
    t = list(map(int, input().split()))
    h = (t[0] + t[2])
    m = (t[1] + t[3])
    if m > 60:
        m -= 60
        h += 1
    if h > 12:
        h -= 12
    print(f"#{tc+1} {h} {m}")