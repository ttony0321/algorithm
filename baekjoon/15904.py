#15904
#그리디 알고리즘
#실버5

words = input().replace(' ', '')
ans = 'UCPC'
idx = 0
for i in words:
    if i == ans[idx]:
        idx += 1
    if idx == 4:
        print('I love UCPC')
        break
else:
    print('I hate UCPC')