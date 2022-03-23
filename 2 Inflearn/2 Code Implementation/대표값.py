# 대표값
# Time Complexity: O(N)

import sys

n=int(input())
a=list(map(int, input().split()))
# round -> 0.5도 내려버림
ave=sum(a)/n
ave=ave+0.5
ave=int(ave)
minn = 2147000000
for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < minn:
        minn = tmp
        score = x
        res = idx + 1
    elif tmp == minn:
        if x > score:
            score = x
            res = idx + 1
print(ave, res)