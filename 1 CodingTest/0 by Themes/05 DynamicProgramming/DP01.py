import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())
warehouse = [0]
warehouse = warehouse + list(map(int, input().split()))

dp = [0] * (n+1)
# 초기값 설정
dp[1] = warehouse[1]
dp[2] = max(warehouse[1], warehouse[2])
# n >= 3
for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + warehouse[i])
print(dp[n])