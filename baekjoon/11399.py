#11399
#그리디 알고리즘
#실버3


n = int(input())#사람 수
time = list(map(int, input().split()))#걸린시간

time.sort()
sum = 0
for i in range(n):
    for j in range(i+1):
        sum += time[j]
print(sum)