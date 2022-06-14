#1541
#그리디 알고리즘, 수학, 문자열, 파싱
#실버 2

m = input().split('-')
answer = 0
for i in m[0].split('+'):
    answer += int(i)

for j in m[1:]:
    for k in j.split("+"):
        answer -= int(k)

print(answer)