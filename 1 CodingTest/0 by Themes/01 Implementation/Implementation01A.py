import sys
import time
sys.stdin = open("input.txt", 'rt')
start_time = time.time()

# 24 * 60 * 60 = 총 연산횟수 86,400 < 100,000
#     -> 3중 for문을 이용한 완전탐색(Brute Forcing)
# Brute Forcing 추천: 연산횟수 <= 1,000,000

n = int(input())

count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k): # 새로운 표현
                count += 1
print(count)

end_time = time.time()
print("time: ", end_time - start_time)