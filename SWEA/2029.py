#2029 D1

n = int(input())
for i in range(n):
    a = b = 0
    j, k = map(int, input().split())
    
    a = int(j/k)
    b = int(j%k)
    print('#{} {} {}'.format(i+1, a, b))