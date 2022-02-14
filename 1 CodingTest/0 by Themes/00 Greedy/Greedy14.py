# 볼링공 고르기
# 이것이 코딩테스트다, p.315

import sys
sys.stdin = open('Greedy14.txt', 'rt')

n, m = map(int, input().split())
balls = list(map(int, input().split()))

weight = [0] * 11
for ball in balls:
    weight[ball] += 1

result = 0
for i in range(1, m+1):
    n -= weight[i]
    result += weight[i] * n
print(result)