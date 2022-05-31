#10610
#그리디 알고리즘
#실버5


#30조건
#뒷자리 0
#각자리 합 = 3


n = str(input())
lst = sorted(n, reverse=True)
sum = 0
if '0' not in n:
    print(-1)
else:
    for i in n:
        sum += int(i)
    if sum%3 !=0:
        print(-1)
    else:
        print(''.join(lst))
