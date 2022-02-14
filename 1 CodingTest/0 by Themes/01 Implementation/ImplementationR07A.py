import sys
import time
start_time = time.time()
sys.stdin = open('input.txt', 'rt')
n = int(input())

ch = [0] * (n+1)
cnt = 0

for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, n+1, i): # 압축된 표현식
            ch[j] = 1
print(cnt)

end_time = time.time()
print('total_time: ', end_time - start_time)