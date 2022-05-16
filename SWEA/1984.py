#1984 D2

n = int(input())
for i in range(n):
    s = 0
    n_l = list(map(int, input().split()))
    n_l.remove(max(n_l))
    n_l.remove(min(n_l))
    avg_n = round(sum(n_l)/len(n_l))
    print(n_l)
    print('#{} {}'.format(i + 1, avg_n))
