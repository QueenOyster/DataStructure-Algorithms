import sys
import time
sys.stdin = open('input.txt', 'rt')
start_time = time.time()

current_data = input()
dx = [-2, -1, +1, +2, +2, +1, -1, -2]
dy = [+1, +2, +2, +1, -1, -2, -2, -1]

cnt = 0
for i in range(8):
    if 1 <= ord(current_data[0])- 96 + dx[i] <= 8 and 1 <= int(current_data[1])+dy[i] <= 8:
        cnt += 1
print(cnt)

end_time = time.time()
print('time: ', end_time - start_time)