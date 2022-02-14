import sys
import time
sys.stdin = open("input.txt", 'rt')
start_time = time.time()

number, maximum_weight = map(int, input().split())
weights = list(map(int, input().split()))
# 그리디 -> 배열 -> 생각할 거리가 줄어든다 or 논리가 명확해진다
weights.sort()

cnt = 0
while weights:
    if len(weights) == 1:
        weights.clear()
    else:
        if weights[-1] + weights[0] <= maximum_weight:
            del weights[0]
        weights.pop()
    cnt += 1

print(cnt)
end_time = time.time()
print("time: ", end_time - start_time)