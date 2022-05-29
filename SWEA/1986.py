#1986 D2

n = int(input())

for j in range(n):
    k = 0
    for i in range(1, int(input())+1):
        if i % 2 == 1:
            k += i
        else:
            k -= i
    print(f'#{j+1} {k}')