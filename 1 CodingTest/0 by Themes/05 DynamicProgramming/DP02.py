import sys
sys.stdin = open('input.txt', 'rt')
n = int(input())
warehouse = [0]
warehouse = warehouse + list(map(int, input().split()))

dp = [0] * (n+1)
# 초기값 설정
dp[1] = warehouse[1]
if warehouse[2] > warehouse[1]:
    last_house = 2
    dp[2] = warehouse[2]
else:
    last_house = 1
    dp[2] = warehouse[1] # 미래 대비 원칙
# n >= 3
for i in range(3, n+1):
    if last_house == i-1:
        if dp[i-1] >= dp[i-2] + warehouse[i]:
            dp[i] = dp[i-1]
        else:
            last_house = i
            dp[i] = dp[i-2] + warehouse[i]
    elif last_house == i-2:
        last_house = i
        dp[i] = dp[i-2] + warehouse[i]
print(dp[n])