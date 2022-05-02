n = int(input())
x = 0
y = 1
z = 0
for i in range(1, n):
    z = x+y
    x = y
    y = z
    
print(y)
