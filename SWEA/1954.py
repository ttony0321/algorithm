#1954 D2
t = int(input())

for i in range(1, t+1):
    n = int(input())
    snail = [[0]*n for _ in range(n)]

    #방향 전환
    dx = [0,1,0,-1]#위아래
    dy = [1,0,-1,0]#좌우
    d = 0
    x = y = 0
    snail[x][y] = 1
    for k in range(2, n**2+1):
        x += dx[d]
        y += dy[d]
        snail[x][y] = k
        if 0 <= x + dx[d] < n and 0 <= y + dy[d] < n and not snail[x + dx[d]][y + dy[d]]:
            continue
        if d != 3:
            d += 1
        else:
            d = 0

    print(f'#{i}')

    for j in snail:
        print(*j)