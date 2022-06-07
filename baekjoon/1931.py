#1931
#그리디 알고리즘, 정렬
#실버 1

n = int(input())
time = []
for i in range(n):
    s, e = map(int, input().split())
    time.append([s, e])

time = sorted(time, key=lambda x: x[0])
time = sorted(time, key=lambda x: x[1])

last = 0
cnt = 0
for i, j in time:
    if i >= last:
        cnt += 1
        last = j

print(cnt)