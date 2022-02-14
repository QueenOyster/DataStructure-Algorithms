import sys
import time
sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n, k = map(int, input().split())
divisor = [0]
for i in range(1, n+1):
    if n % i == 0:
        divisor.append(i)
if len(divisor)-1 >= k:
    print(divisor[k])
else:
    print(-1)
    
end_time = time.time()
print('time: ', end_time - start_time)