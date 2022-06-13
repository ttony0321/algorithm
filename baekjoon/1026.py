#1026
#브루트포스 알고리즘, 정렬, 수학
#실버 4

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


a = sorted(a, reverse=True)
b = sorted(b, reverse=False)

sum = 0
for i in range(n):
    sum += a[i] * b[i]

print(sum)