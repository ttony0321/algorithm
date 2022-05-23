#1989 D2

n = int(input())
for tc in range(n):
    word = input()
    ans = 0
    if word == word[::-1]:
        ans = 1
    else:
        ans = 0
    print(f"#{tc+1} {ans}")