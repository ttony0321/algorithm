#2072 D1
n = int(input())
for tc in range(n):
    tc_lst = map(int, input().split())
    cnt = 0
    for i in tc_lst:
        if i%2 != 0:
            cnt += i
    print(f"#{tc+1} {cnt}")