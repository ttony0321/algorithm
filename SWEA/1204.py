#1204 D2

N = int(input())

for tc in range(N):
    tcn = int(input())
    scores = list(map(int, input().split()))
    ans = 0
    for i in range(len(scores)):
        if scores.count(i) == 0:
            continue
        elif scores.count(i) >= scores.count(ans):
            ans = i

    print(f'#{tc+1} {ans}')

