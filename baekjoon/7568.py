#7568
#브루트포스 알고리즘, 구현
#실버 4

n = int(input())
size = []
for _ in range(n):
    w, h = map(int, input().split())
    size.append([w, h])


ans = []
for i, j in size:
    cnt = 1
    for x, y in size:
        if x > i and y > j:
            cnt += 1
    ans.append(cnt)
print(*ans)