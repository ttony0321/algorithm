#2217
#그리디 알고리즘, 정렬, 수학
#실버 4

n = int(input())
n_list = []
for i in range(n):
    n_list.append(int(input()))

n_list.sort(reverse=True)
ans = []
for j in range(n):
    ans.append(n_list[j]* (j+1))

print(max(ans))