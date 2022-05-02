#1938 D1

a, b = map(int, input().split())

if a >= b:
    c = a/b
else:
    c = b/a
print(a+b)
print(abs(a-b))
print(a*b)
print(int(c))