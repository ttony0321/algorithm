#1966 D2

n = int(input())
for i in range(n):
    c = int(input())
    num = list(map(int, input().split()))
    s_num = sorted(num)

    print(f"#{i+1} ", end='')
    print(*s_num)
