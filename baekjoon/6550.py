#6550
#그리디 알고리즘
#실버5
while True:
    try:
        s, t = map(str, input().split())
        idx = 0
        check = 'No'
        for i in t:
            if i == s[idx]:
                idx += 1
                if idx == len(s):
                    check = 'Yes'
                    break
        print(check)

    except:
        break#('런타임 에러 처리')