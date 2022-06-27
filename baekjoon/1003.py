#1003
#다이나믹 프로그래밍
#수학

n = int(input())
lst = []
for _ in range(n):
    cnt_ze = [1, 0]
    cnt_on = [0, 1]
    n = int(input())
    if n > 1:
        for i in range(n-1):
            cnt_ze.append(cnt_on[-1])
            cnt_on.append(cnt_ze[-2] + cnt_on[-1])
    print(cnt_ze[n], cnt_on[n])
