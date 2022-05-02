n = int(input())  
test_list = list(map(int, input().split()))
sum_n = 0
list_max = max(test_list)
for i in test_list:
    t =i/list_max*100
    sum_n += t
    
print(sum_n / n)