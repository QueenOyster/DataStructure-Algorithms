import sys
import time
from collections import deque
sys.stdin = open("input.txt", 'rt')
start_time = time.time()

n = int(input())
series = list(map(int, input().split()))
series = deque(series)
series.appendleft(0)

result = []
for i in range(n, 0, -1):
    result.insert(series[i], i)

print() #
for x in result:
    print(x, end=' ')
print()

end_time = time.time()
print("time: ", end_time - start_time)
print() #