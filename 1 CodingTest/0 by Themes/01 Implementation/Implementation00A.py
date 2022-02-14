import sys
import time
sys.stdin = open("input.txt", 'rt')
start_time = time.time()

n = int(input())
x, y = 1, 1
# map을 쓰지 않아도 표현 가능
plans = input().split() 

# 격자 방향 이동에 dx, dy 이용
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i] and 1<= x + dx[i] <= n and 1<= y + dy[i] <= n:
            x = x + dx[i]
            y = y + dy[i]
            break

print(x, y)
end_time = time.time()
print("time: ", end_time - start_time)