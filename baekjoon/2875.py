#2875
#수학, 구현, 사칙연산
#브론즈 3


n, m, k = map(int, input().split())

team = 0

while n >= 2 and m >= 1 and n + m - k >= 3:
    n -= 2
    m -= 1
    team += 1
print(team)