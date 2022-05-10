#2005 D2

from unittest import result


t = int(input())

for i in range(1, t+1):
    n = int(input())
    
    lst = [[0]* n for _ in range(n)]
    for j in range(n):
        for k in range(j + 1):
            if k == 0 or k == j:
                lst[j][k] = 1   #양끝 은 1
            else:
                lst[j][k] = lst[j-1][k] + lst[j-1][k-1]
    print('#{}'.format(i))
    #0 만 출력
    for s in lst:
        r = [q for q in s if q]
        #리스트 안의 내용만 출력
        print(*r)