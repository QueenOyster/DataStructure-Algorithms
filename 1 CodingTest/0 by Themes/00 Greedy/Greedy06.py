import sys
import time
sys.stdin = open("input.txt", 'rt')
start_time = time.time()

L = int(input())
levels = list(map(int, input().split()))
M = int(input())

levels.sort()

for _ in range(M):
    levels[L-1] -= 1
    levels[0] += 1
    i = 0
    while True:
        if levels[L-2-i] > levels[L-1-i]:
            levels[L-2-i], levels[L-1-i] = levels[L-1-i], levels[L-2-i]
            i += 1
        else:
            break
    i = 0
    while True:
        if levels[0+i] > levels[1+i]:
            levels[0+i], levels[1+i] = levels[1+i], levels[0+i]
            i += 1
        else:
            break
print()
print("answer: ", levels[L-1]-levels[0])

end_time = time.time()
print("time: ", end_time-start_time)
print()