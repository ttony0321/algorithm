#1936 D1

#가위 1  바위 2  보  3

a,b = map(int, input().split())

rpc_dict = {1:3, 2:1, 3:2}
if rpc_dict[a] == b:
    print('A')
else:
    print('B')