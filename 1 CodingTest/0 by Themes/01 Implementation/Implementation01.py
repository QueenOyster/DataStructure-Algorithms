import sys
import time
sys.stdin = open("input.txt", 'rt')
start_time = time.time()

n = int(input())
cnt = 0
for i in range(0, n+1):
    if i % 10 == 3:
        cnt += 3600
    else: # 여집합 논리
        cnt += (3600 - 5*9*5*9)
print(cnt)

end_time = time.time()
print("time: ", end_time - start_time)