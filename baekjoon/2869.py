a, b, v = map(int, input().split())

f = (v - b)%(a-b)
c = (v - b)/(a-b)
if f == 0:
    print(int(c))
else:
    print(int(c+1))
    
