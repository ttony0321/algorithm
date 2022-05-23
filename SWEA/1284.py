#1284 D2

"""

A사 1L당 요금 : P
B사 RL 이하 요금 : Q , RL 이후 1L 당 S
자신이 사용한 수도의 양 : W
"""
n = int(input())
for tc in range(n):
    P, Q, R, S, W = map(int, input().split())
    a = W * P
    b = Q
    if R < W:
        b += S * abs(R-W)

    cost = min(a, b)
    print(f'#{tc + 1} {cost}')



