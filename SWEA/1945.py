#1945 D2

##인풋
n = int(input())
n_lst = []
n_o = [2, 3, 5, 7, 11]   


for i in range(n):
    nc = int(input())
    n_s = [0, 0, 0, 0, 0]
    for j in range(5):
        while True:
            if(nc % n_o[j] == 0):
                n_s[j] += 1
                nc //= n_o[j]
            else:
                break
    print('#{} {}'.format(i + 1, " ".join(map(str, n_s))))