import sys
import time
start_time = time.time()
sys.stdin = open('input.txt', 'rt')
n = int(input())

checking = [0] * (n+1)
for i in range(2, n+1):
    k = 1
    while k*i <= n:
        checking[k*i] += 1
        k += 1

cnt = 0
for repeated in checking:
    if repeated == 1:
        cnt += 1
print(cnt)

end_time = time.time() # 같은 변수 중복 사용 조심
print('total_time: ', end_time - start_time)  # 시간 더 줄일 수 있다.