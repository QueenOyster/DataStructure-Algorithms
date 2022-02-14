import sys
import time
sys.stdin = open('input.txt', 'rt')
start_time = time.time()

n, k = map(int, input().split())
cards = list(map(int, input().split()))
values = list()
for i in range(n):
    for j in range(i+1, n):
        for l in range(j+1, n): # index 주의
            value = cards[i] + cards[j] + cards[l]
            values.append(value)
values = set(values)
values = list(values)
values.sort(reverse=True)
# print(values)
print(values[k-1])

end_time = time.time()
print('time: ', end_time - start_time)