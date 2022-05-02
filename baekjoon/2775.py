a_list = [[0 for i in range(14)] for j in range(15)]
for i in range(15):
    a_list[i][0] = 1
for i in range(14):
    a_list[0][i] = i + 1
for i in range(1, 15):
    for j in range(1,14):
        a_list[i][j] = a_list[i-1][j] + a_list[i][j-1]
    
T_case = int(input())
for i in range(T_case):
    k = int(input())
    n = int(input())
    print(a_list[k][n-1])