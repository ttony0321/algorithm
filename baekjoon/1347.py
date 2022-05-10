#1347 실버 3

#시작 남쪽 바라보는거기준
#남쪽 기준이라 L이면 오른족 R이면 왼쪽


n = int(input())

move = input().strip()

start_loc = [(0,0)]

x = [1,0,-1,0]
y = [0,1,0,-1]

dir = 0 #남쪽 바라보는 기준

for i in move:
    if i == 'R':
        dir = (dir + 3)%4        #보는 방향 <-
    elif i == 'L':
        dir = (dir + 1)%4       #보는 방향 ->
    else:
        dx = start_loc[-1][0] + x[dir]
        dy = start_loc[-1][1] + y[dir]
        start_loc.append((dx, dy))
        
x_sort = sorted(start_loc, key=lambda x: x[0])
y_sort = sorted(start_loc, key=lambda x: x[1])
x_min, x_max = x_sort[0][0], x_sort[-1][0]
y_min, y_max = y_sort[0][1], y_sort[-1][1]


m_list = [["#" for y in range(y_min, y_max + 1)]for x in range(x_min, x_max + 1)]

for i in range(len(start_loc)):
    start_loc[i] = (start_loc[i][0] - x_min, start_loc[i][1] - y_min)
    
for i, j in start_loc:
    m_list[i][j] = '.'
    
for r in m_list:
    print(''.join(r))  