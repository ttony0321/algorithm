#1215 D3
t = 10
for tc in range(t):
    #회문길이
    n =int(input())
    pal = [list(input()) for _ in range(8)]
    cnt = 0

    #가로
    for i in range(8):  #세로축
        for j in range(8-n+1):
            if pal[i][j:j+n] == pal[i][j:j+n][::-1]:
                cnt += 1
    #세로
    for j in range(8):
        for i in range(8-n+1):
            char = ''
            for k in range(i, i+n):
                char += pal[k][j]
            if char == char[::-1]:
                cnt +=1

    print(f'#{tc+1} {cnt}')
