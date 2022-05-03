#2071 D1
from audioop import avg


n = int(input())

for i in range(1, n+1):
    sum = 0
    lst = list(map(int, input().split()))
    for j in lst:
        sum += j
    print("#{} {}".format(i, round(sum/len(lst))))
