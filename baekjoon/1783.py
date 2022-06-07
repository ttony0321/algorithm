#1783
#그리디 알고리즘
#실버 4


n, m= map(int, input().split())
#가로 m, 세로 n

if n == 1:
    cnt = 1
elif n == 2:
    cnt = min(4, (m-1)//2+1)
elif m < 7:
    cnt = min(4, m)
else:
    cnt = (2+(m-5)) + 1

print(cnt)