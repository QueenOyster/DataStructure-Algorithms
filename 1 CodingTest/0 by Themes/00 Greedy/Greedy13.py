# 만들 수 없는 금액
# 이것이 코딩테스트다, 314pg

import sys
sys.stdin = open('Greedy13.txt', 'rt')

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

if coins[0] >= 2:
    result = 1
else:
    result = 1
    for coin in coins:
        if result < coin:
            break
        result += coin
print(result)