#1120
#그리디 알고리즘, 구현, 문자열
#실버 4

a, b = input().split()
ans = []

for i in range(len(b) - len(a) + 1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt += 1
    ans.append(cnt)

print(min(ans))