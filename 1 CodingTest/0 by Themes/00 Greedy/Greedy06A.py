import time
import sys
sys.stdin = open("input.txt", 'rt')
start_time = time.time()

L = int(input())
a = list(map(int, input().split()))
m = int(input())
a.sort()
for _ in range(m):
    a[0] += 1
    a[L-1] -= 1
    # sort를 써도 나의 풀이와 소요 시간은 거의 동일.
    a.sort()
print(a[L-1]-a[0])

end_time = time.time()
print("time: ", end_time-start_time)