#2007 D2

n = int(input())
for tc in range(n):
    s = str(input())
    for i in range(1,10):
        if s[:i] == s[i:2*i]:
            # AD    ADAD
            # ABD   ABDABD
            print(f"#{tc+1} {i}")
            break