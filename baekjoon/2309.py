n_list = []
ans = []
n_sum = 0
for i in range(9):
    n_list.append(int(input()))
n_list.sort()

t = sum(n_list)
for i in range(9):
    for j in range(i+1, 9):
        if t - (n_list[i]+ n_list[j]) == 100:
            a = n_list[i]
            b = n_list[j]

n_list.remove(a)
n_list.remove(b)
for i in n_list:
    print(i)