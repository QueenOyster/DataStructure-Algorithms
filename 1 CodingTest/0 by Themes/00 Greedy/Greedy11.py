# 이것이 코딩테스트다, p.312
# 0, 1 or 2~9
# 손으로 써보면서 규칙성 파악 할 것!

import sys
from collections import deque
sys.stdin = open('Greedy11.txt', 'rt')
s = list(str(input()))
s = deque(s)
# print(s)

result = 0
while s:
    now = int(s.popleft())
    if result <= 1:
        result += now
    else:
        if now >= 2:
            result *= now
        else:
            result += now
print(result)
