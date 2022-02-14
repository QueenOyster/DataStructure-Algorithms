import sys
import time
sys.stdin = open('input.txt', 'rt')
start_time = time.time()

t = int(input())
for i in range(t):
    n, s, e, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    new_numbers = numbers[s-1:e]
    new_numbers.sort()
    result = new_numbers[k-1] # 없어도 됨
    print('#%d %d' %(i+1, result))


end_time = time.time()
print('time: ', end_time - start_time)