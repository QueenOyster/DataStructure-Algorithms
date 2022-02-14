# 이것이 코딩테스트다, p.311

import sys
from collections import deque
sys.stdin = open('Greedy10.txt', 'rt')
n = int(input())

adventurers = list(map(int, input().split()))
adventurers.sort()
adventurers = deque(adventurers)

cnt = 0
temp_group = list()
while adventurers:
    max_fear_value = adventurers.popleft()
    temp_group.append(max_fear_value)
    if temp_group[-1] <= len(temp_group):
        # print(temp_group)
        temp_group.clear()
        cnt += 1
    else:
        continue
print(cnt)