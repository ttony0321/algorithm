#19539
#그리디 알고리즘
#수학

n = int(input())
lst = list(map(int, input().split()))
a, b = divmod(sum(lst), 3)

cnt = 0

if b == 0:
    for i in lst:
        cnt += i // 2

    if cnt >= a:
        print("YES")
    else:
        print("NO")

else:
    print("NO")