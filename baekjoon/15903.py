#15903
#그리디 알고리즘, 자료구조, 우선순위 큐
#실버 1

m, n = map(int, input().split())

k = list(map(int, input().split()))


for i in range(n):
    k.sort()
    s = k[0] + k[1]
    k[0] = s
    k[1] = s

print(sum(k))